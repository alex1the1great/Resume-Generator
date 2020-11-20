from docx import Document

document = Document()

# section: user basic info.
name = input('Enter your full name: ')
document.add_heading(name)

user_info = document.add_paragraph()

address = input('Enter your address: ')
user_info.add_run(address + '\n').italic = True

email = input('Enter your email: ')
user_info.add_run(email + '\n')

phone_number = input('Enter your phone number: ')
user_info.add_run(phone_number)

# section: user bio.
document.add_heading('Career Profile')
user_bio = input('Describe yourself: ')
document.add_paragraph(user_bio)

# section: skills
document.add_heading('Skills')

while True:
    has_skill = input('Do you have skill: (y/n) ')

    if has_skill.lower() == 'y':
        skill_name = input('Enter your skill name: ')
        document.add_paragraph(skill_name, 'List Bullet')
    else:
        break

document.save('cv.docx')
