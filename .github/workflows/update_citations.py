from scholarly import scholarly
import json

scholar_id = "IcwW-WAAAAAJ"

# Fetch author profile
author = scholarly.search_author_id(scholar_id)
print("Author found")
author = scholarly.fill(author, sections=["indices"])

# Get total citations
citations = author["citedby"]
print("Citation parsed")

# Write to file
with open("citations.json", "w") as f:
    json.dump({"citations": citations}, f)
