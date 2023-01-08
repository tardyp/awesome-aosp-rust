#!/usr/bin/env python3
import glob
import re
import textwrap
import psycopg2
import os
import pathlib
from collections.abc import Generator

# this script should be run "under lunch"
top = pathlib.Path(os.getenv("ANDROID_BUILD_TOP"))

# Find all METADATA files
metadata_files = glob.glob(str(top / "external/rust/crates/*/METADATA"))

# This can be setup using import_cargo_db.sh
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password=os.getenv("POSTGRES_PASSWORD"),
)

crates = {}
categories = {}

name_regex = re.compile(r"name\s*:\s*\"(.+?)\"")
description_regex = re.compile(r"description\s*:\s*\"(.+?)\"")
url_regex = re.compile(r"value\s*:\s*\"(.+?)\"")

# Iterate over each METADATA file
for metadata_file in metadata_files:
    with open(metadata_file, "r") as f:
        contents = f.read()

    name_match = name_regex.search(contents)
    name = name_match.group(1) if name_match else "(unknown)"
    description_match = description_regex.search(contents)
    description = description_match.group(1) if description_match else "(none)"
    urls = set(url_regex.findall(contents))
    cur = conn.cursor()
    cur.execute(
        f"""
    select homepage, documentation, repository, description
    from crates 
    where name = '{name}';"""
    )
    row = cur.fetchone()

    if row is not None:
        if row[3]:
            description = row[3]
        for url in row[:-1]:
            if url:
                urls.add(url)
        crates[name] = dict(name=name, description=description, urls=urls)

    cur.execute(
        f"""
    select categories.category
    from crates 
    left join crates_categories on crates_categories.crate_id = crates.id 
    left join categories on crates_categories.category_id  = categories.id
    where name = '{name}';"""
    )
    row = cur.fetchone()

    while row is not None:
        cat = row[0]
        if cat is not None:
            categories.setdefault(cat, set())
            categories[cat].add(name)
        row = cur.fetchone()

# don't really care about this category for AOSP
del categories["No standard library"]


rustlibs_re = re.compile(r"rustlibs:\s*\[(.*?)\]", re.MULTILINE | re.DOTALL)
stripcomments_re = re.compile(r"/\*.?\*/|//.*$", re.MULTILINE)


def find_rust_android_bp(d) -> Generator[pathlib.Path]:
    for root, dirs, files in os.walk(top / d, topdown=False):
        for name in files:
            if name == "Android.bp":
                yield pathlib.Path(root) / name


# find first order dependencies by matching rustlibs in Android.bp files
rustlibs = dict()
rustcomponents = dict()
for d in ["device", "hardware", "packages", "system"]:
    for bp in find_rust_android_bp(d):
        text = bp.read_text()
        if "rustlibs" in text:
            text = stripcomments_re.sub("", text)
            component = str(bp.parent).replace(str(top) + "/", "")
            rustcomponents.setdefault(component, set())

            for match in rustlibs_re.finditer(text):
                rustlib_string = match.group(1)
                for rustlib in rustlib_string.split(","):
                    rustlib = rustlib.strip(' "\t\n').lstrip("lib")
                    rustlibs.setdefault(rustlib, set())
                    if rustlib:
                        rustlibs[rustlib].add(component)
                        rustcomponents[component].add(rustlib)

def to_anchor(c):
    return c.replace(" ", "-").replace(":", "").lower()

with open("README.md", "w") as summary_file:
    summary_file.write(textwrap.dedent("""
    # Intro

    List of rust libraries, currated by AOSP rust developers.
    Script available in this repo finds the rust libraries in a aosp tree, sorted by crates.io categories
    End of the file, you can also find the list of aosp component written in rust along with the open source libraries that they use

    # Contents

    """))


    summary_file.write("## available crates sorted by categories\n\n")

    # generate ToC with all categories
    for cat in sorted(categories):
        cat_anchor = to_anchor(cat)
        summary_file.write(f"- [{cat}](#{cat_anchor})\n")

    summary_file.write("\n")

    summary_file.write("## [AOSP rust components](#rust-components-found-in-aosp)\n\n")

    summary_file.write("# Crates\n\n")

    for cat, _crates in sorted(categories.items()):

        summary_file.write(f"## {cat}\n\n")

        for name in sorted(_crates):
            summary_file.write(f"### {name}\n\n")
            summary_file.write(f"<details><summary>\n")
            summary_file.write(f"{crates[name]['description']}\n\n")
            summary_file.write(f"</summary>\n\n")
            for url in sorted(crates[name]["urls"]):
                if not url.startswith("https://static.crates.io"):
                    summary_file.write(f"- {url}\n")
            summary_file.write(f"\n</details>")
            if name in rustlibs:
                summary_file.write(f"<details><summary>\n")
                summary_file.write(f"{len(rustlibs[name])} uses\n\n")
                summary_file.write(f"</summary>\n\n")
                for d in sorted(rustlibs[name]):
                    summary_file.write(
                        f"- [{d}](https://cs.android.com/android/platform/superproject/+/master:{d})\n"
                    )
                summary_file.write(f"\n</details>")
            summary_file.write("\n\n")

    summary_file.write("\n\n# rust components found in AOSP\n\n")

    for component, _crates in sorted(rustcomponents.items()):
        summary_file.write(
            f"- [{component}](https://cs.android.com/android/platform/superproject/+/master:{component})"
        )
        __crates = [f"[{c}](#{to_anchor(c)})" for c in _crates if c in sorted(crates)]
        if __crates:
            summary_file.write(
                f'({", ".join(__crates)})'
            )
        summary_file.write("\n")
    print(f"{summary_file.name} written!")

