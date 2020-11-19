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
user_info.add_run(phone_number + '\n')


document.save('cv.docx')
