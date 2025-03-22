from flask import Flask, render_template_string

app = Flask(__name__)

personal_info = {
    'name': 'Tatatharanidaran R R',
    'email': 'rtata205@gmail.com',
    'phone': '8148331609',
    'address': 'Namakkal'
}

career_info = {
    'current_job': 'Student',
    'skills': ['Docker', 'Kubernetes', 'Terraform', 'AWS', 'SQL'],
    'certification': 'Acquired a certificate in Cloud fest, a workshop conducted for Cloud AWS',
    'education': 'Bachelor of Technology in Information Technology'
}

landing_page_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page</title>
</head>
<body>
    <h1>Welcome to My Personal Website</h1>
    
    <h2>Personal Information</h2>
    <ul>
        <li><strong>Name:</strong> {{ personal_info['name'] }}</li>
        <li><strong>Email:</strong> {{ personal_info['email'] }}</li>
        <li><strong>Phone:</strong> {{ personal_info['phone'] }}</li>
        <li><strong>Address:</strong> {{ personal_info['address'] }}</li>
    </ul>

    <p><a href="/career">Click here to see my career information</a></p>
</body>
</html>
"""

career_page_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Career Information</title>
</head>
<body>
    <h1>My Career Information</h1>
    
    <ul>
        <li><strong>Current Job:</strong> {{ career_info['current_job'] }}</li>
        <li><strong>Skills:</strong>
            <ul>
                {% for skill in career_info['skills'] %}
                    <li>{{ skill }}</li>
                {% endfor %}
            </ul>
        </li>
        <li><strong>Certification:</strong> {{ career_info['certification'] }}</li>
        <li><strong>Education:</strong> {{ career_info['education'] }}</li>
    </ul>

    <p><a href="/">Back to Personal Information</a></p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(landing_page_html, personal_info=personal_info)

@app.route('/career')
def career():
    return render_template_string(career_page_html, career_info=career_info)

if __name__ == '__main__':
    app.run(debug=True)

