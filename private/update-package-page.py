
if __name__ == "__main__":
    import sys
    import os
    import json
    from typing import List

    package_name: str = sys.argv[1]
    package_version: str = sys.argv[2]
    package_actual_name: str = sys.argv[3]
    package_project_name: str = sys.argv[4]
    package_source_directory: str = sys.argv[5]


    with open("./" + package_name + "/versions.json", "r+") as f:
        versions_json = json.load(f)
        f.seek(0)
        if package_version in versions_json:
            print("version has already been uploaded", file=sys.stderr)
            exit(1)
        sub_directory: str = "" if package_source_directory == "." else f"subdirectory={package_source_directory}&"
        versions_json[package_version] = f"<a href=\"git+ssh://git@gitlab.com/{package_project_name}@{package_version}{sub_directory}#egg={package_actual_name}-{package_version}\">{package_actual_name}-{package_version}</a>"
        f.write(json.dumps(versions_json))
    
    version_list_html: str = ""

    for version in versions_json:
        version_list_html += """  <li>
	    """ + versions_json[version] + """
      </li>
        """

    page_html: str = """<!DOCTYPE html>
<html>
  <head>
    <title>Links for """ + package_actual_name + """</title>
  </head>
  <body>
    <h1>Links for """+ package_actual_name + """</h1>
    <ul>
    """ + version_list_html + """
    </ul>
  </body>
</html>"""
    print(page_html)
    with open("./" + package_name + "/index.html", "w") as f:
        f.write(page_html)