
if __name__ == "__main__":
    import sys
    import os
    import json
    from typing import List

    package_name: str = sys.argv[1]

    with open("./packages.json", "r+") as f:
        packages_json = json.load(f)
        f.seek(0)
        if package_name in packages_json["packages"]:
            exit(0)
        packages_json["packages"].append(package_name)
        os.mkdir(package_name)
        with open(package_name + "/versions.json", "w") as f2:
            f2.write("{}")
        f.write(json.dumps(packages_json))
    
    folder_structure_html = ""
    
    packages: List[str] = packages_json["packages"]
    packages.sort()

    for package in packages:
        folder_structure_html += """<div class="package" >
	    <a href=\"""" + package + "/\">" + package + """</a>
	</div>
        """

    front_page_html: str = """<!DOCTYPE html>
<html>
<head>
    <title>Cyberspace Python Package Index</title>
    <style>
        body {
        font-family: "Source Sans Pro", "Trebuchet MS", "Lucida Grande", "Bitstream Vera Sans", "Helvetica Neue", "sans-serif";
        margin: 0px;
        }
        h1 {
        background-color: rgba(130,174,182,1);
        font-size: 24px;
        color: rgba(4,38,45,1);
        padding: 20px;
        }	
        .explanation {
        background-color: rgba(215,226,241,1);
        font-size: 14px;
        color: rgba(4,38,45,1);
        padding: 20px;
        }
        div.package {
        font-size: 16px;
        color: rgba(79,108,142,1);
        border-bottom: 5px solid rgba(215,227,241,1);
        padding: 20px;
        width: 100%;
        }		
</style>
</head>
<body>
    <h1>Cyberspace Python Package Index</h1>
    <section class="explanation">
        <p>This is Cyberspace python package index. Hosts packages for Python.</p>
    </section>
    """ + folder_structure_html + """ 
</body>
</html>"""

    with open("./index.html", "w") as f:
        f.write(front_page_html)