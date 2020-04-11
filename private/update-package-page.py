
if __name__ == "__main__":
    import sys
    import os
    import json
    from typing import List

    package_name: str = sys.argv[1]
    package_version: str = sys.argv[2]
    package_actual_name: str = sys.argv[3]

    with open("./" + package_name + "/versions.json", "r+") as f:
        versions_json = json.load(f)
        f.seek(0)
        if package_version in versions_json:
            print("version has already been uploaded", file=sys.stderr)
            exit(1)
        packages_json[package_version] = f"<a href=\"git+https://gitlab.com/zigseg/iot-core/-/tree/develop/python/ModuleFramework#egg={package_actual_name}-{package_version}\">{package_actual_name}-{package_version}</a><br/>"
    
    folder_structure_html = ""
    
    packages: List[str] = packages_json["packages"]
    packages.sort()

    for package in packages:
        folder_structure_html += """<div class="package" >
	    <a href=\"""" + package + "/\">" + package + """</a>
	</div>
        """

    page_html: str = """<!DOCTYPE html>
<html>
  <head>
    <title>Links for python_world</title>
  </head>
  <body>
    <h1>Links for """+ python_world + """</h1>
    """ + links +
  """
  </body>
</html>"""

    with open("./" + package_name + "/index.html", "w") as f:
        f.write(page_html)