from spacy.matcher import PhraseMatcher
from utils.nlp_engine import get_nlp

nlp = get_nlp()

TECH_SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "html",
    "css",
    "javascript",
    "flask",
    "django",
    "react",
    "nodejs",
    "git",
    "github",
    "machine learning",
    "deep learning",
    "nlp",
    "data science",
    "rest api",
    "docker",
    "kubernetes",
    "aws",
    "azure"
]

matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp.make_doc(skill) for skill in TECH_SKILLS]
matcher.add("TECH_SKILLS", patterns)


def extract_nlp_skills(text):
    doc = nlp(text)

    matches = matcher(doc)

    found = set()

    for _, start, end in matches:
        found.add(doc[start:end].text.title())

    return sorted(found)