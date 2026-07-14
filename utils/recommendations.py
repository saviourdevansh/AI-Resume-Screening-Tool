def generate_recommendations(missing_skills):

    skill_messages = {
        "python": "Improve your Python programming skills.",
        "java": "Practice Core Java and Object-Oriented Programming.",
        "c++": "Practice Data Structures and Algorithms using C++.",
        "html": "Strengthen your HTML fundamentals.",
        "css": "Improve your CSS styling skills.",
        "javascript": "Learn modern JavaScript (ES6+).",
        "react": "Build projects using React.",
        "nodejs": "Learn backend development using Node.js.",
        "flask": "Build at least one Flask project.",
        "django": "Learn Django framework.",
        "sql": "Practice SQL queries and database design.",
        "mysql": "Learn MySQL database management.",
        "mongodb": "Practice MongoDB and NoSQL databases.",
        "git": "Learn Git version control.",
        "github": "Upload your projects regularly on GitHub.",
        "machine learning": "Study Machine Learning algorithms and build ML projects.",
        "deep learning": "Learn Deep Learning using TensorFlow or PyTorch.",
        "nlp": "Practice Natural Language Processing projects.",
        "data science": "Work on Data Science projects using Python.",
        "oop": "Improve your Object-Oriented Programming concepts.",
        "rest api": "Build REST APIs using Flask or FastAPI."
    }

    recommendations = []
    added = set()

    for skill in missing_skills:

        key = skill.strip().lower()

        if key in skill_messages:

            message = skill_messages[key]

        else:

            message = f"Improve your {skill.title()} skill."

        if message not in added:
            recommendations.append(message)
            added.add(message)

    if len(recommendations) == 0:
        recommendations.append(
            "Excellent Resume! No major skill gaps found."
        )

    return recommendations