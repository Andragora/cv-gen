#convert yaml data to html
import jinja2, yaml
templateFilePath= jinja2.FileSystemLoader('./')
jinjaEnv=jinja2.Environment (loader=templateFilePath)
jTemplate=jinjaEnv.get_template("cv_template.txt")
with open("ur_data.yaml") as config:
    config = yaml.load(config)
    output=jTemplate.render(config)
print(output)
outFileH=open('cv.html', 'w')
outFileH.write(output)
outFileH.close()

#html to pdf
import pdfkit
pdfkit.from_file('cv.html', 'cv.pdf')