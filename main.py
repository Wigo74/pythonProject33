from flask import Flask
import utils
app = Flask(__name__)


@app.route('/')
def page_all_candidates():
    candidates = utils.candidates_get_all()
    list_of_candidates = ""
    for candidate in candidates:
        list_of_candidates += f"{candidate['name']}\n"
        list_of_candidates += f"{candidate['skills']}\n"
        list_of_candidates += f"{candidate['position']}\n"
        list_of_candidates += "\n"
    return "<pre>" + list_of_candidates + "</pre>"


@app.route('/skills/<skill>')
def page_candidates_by_skill(skill):
    candidates = utils.candidates_get_by_skill(skill)
    list_of_candidates = ""
    for candidate in candidates:
        list_of_candidates += f"{candidate['name']}\n"
        list_of_candidates += f"{candidate['skills']}\n"
        list_of_candidates += f"{candidate['position']}\n"
        list_of_candidates += "\n"
    return "<pre>" + list_of_candidates + "</pre>"


@app.route('/candidates/<int:pk>')
def page_candidates_by_pk(pk):
    candidate = utils.candidates_get_by_pk(pk)
    list_of_candidate = ""
    list_of_candidate += f"<img src=\"{candidate['picture']}\">\n"
    list_of_candidate += f"{candidate['name']}\n"
    list_of_candidate += f"{candidate['skills']}\n"
    list_of_candidate += f"{candidate['position']}\n"
    list_of_candidate += "\n"
    return "<pre>" + list_of_candidate + "</pre>"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7000, debug=True)

