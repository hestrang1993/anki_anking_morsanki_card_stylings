# Open the debug console with Ctrl+: (which is Ctrl+Shift+; on US keyboards)
# (Don't have the browser window open when you do.)
# Run it with Ctrl+Enter
# Remove the # from the last line to actually save the changes

search = r'regular expression to search for goes here'
"""
str: The regexp to search for in the source field
"""
replace = ""
"""
str: The string to replace the search regex with
"""
source_field = 'Source Field Name goes here'
"""
str: The name of the source field
"""
target_field = 'Target Field Name goes here'
"""
str: The name of the target field
"""
note_type = 'Name of the Note Type goes here'
"""
str: The name of the note type
"""

# Get the model, and then the list of notes of that type
the_model = mw.col.models.byName(note_type)
"""
object: The model to search
"""
the_notes = mw.col.models.nids(the_model)
"""
list[object]: The list of notes of note_type in the model
"""

def _get_note_content(note_id):
    return mw.col.getNote(notes)


def _search_the_source_field_for_regex(search, note, source_field):
    return re.search(search, note[source_field])



# Run through the list of notes
for nid in the_notes:
    # Get the note contents
    note = mw.col.getNote(nid)
    # Search the source field for the regexp
    m = re.search(search, note[source_field])
    # If there's a match...
    if (m):
        # ... show what it found
        print(m.group(0))
        # ... add it to the target field (comment out if just clearing unwanted content)...
        note[target_field] = m.group(0)
        # ... and remove it from the source field
        note[source_field] = re.sub(search, '', note[source_field])
        # save the changes
        # note.flush()
