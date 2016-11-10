#!/usr/bin/python

# Ripped from philipkglass on HN: https://news.ycombinator.com/item?id=12914188

target = "/usr/bin/spotify"
with open(target) as infile:
    bytes = infile.read()
with open("./spotify", "wb") as backup:
    backup.write(bytes)
fixed = bytes.replace("VACUUM;", "xxxxxx;")
with open (target, "wb") as outfile:
    outfile.write(fixed)
