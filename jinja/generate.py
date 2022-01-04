from jinja2 import Environment, PackageLoader
import os

root = os.path.dirname(os.path.abspath(__file__))

env = Environment(loader=PackageLoader('app'))
template = env.get_template('morsanki_bootstrap_accordion_back.html')

root = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(
    root, 'html', 'morsanki_bootstrap_accordion_back.html')

fields_dict = {
    "Lecture Notes": "lecture-notes",
    "Extra": "extra",
    "First Aid": "first-aid",
    "Boards and Beyond": "boards-and-beyond",
    "Pathoma": "pathoma",
    "Draw It to Know It": "draw-it-to-know-it",
    "AMBOSS": "amboss",
    "Osmosis": "osmosis",
    "OnlineMedEd": "onlinemeded",
    "Sketchy": "sketchy",
    "Pixorize": "pixorize",
    "Missed Questions": "missed-questions",
    "Physeo": "physeo",
    "Additional Resources": "additional-resources",
    "Tags": "tags"
}

field_titles_list = []
fields_list = []
for field_title, field in fields_dict.items():
    field_titles_list.append(field_title)
    fields_list.append(field)

left_bracket = "{{"
right_bracket = "}}"
fields_cloze_list = [f"{left_bracket}{field_title}{right_bracket}" for field_title in field_titles_list]

print(fields_cloze_list)

with open(filename, 'w') as fh:
    fh.write(template.render(
        fields_dict = fields_dict,
        left_bracket = left_bracket,
        right_bracket = right_bracket
    ))
