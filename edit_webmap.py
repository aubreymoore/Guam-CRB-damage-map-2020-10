"""
Tweeks a web map which has been generated by qgis2web and stored in index.html
Output is saved in new_index.html

Usage:

    python3 edit_webmap.py

Aubrey Moore 202-10-29
"""

import re

# Add project abstract
abstract =  '<b>Coconut Rhinoceros Beetle Damage</b><br>'
abstract += '<b>Guam Roadside Video Survey 1</b><br><br>'
abstract += '<table>'
abstract += '<tr><td>Start date:</td><td  style="text-align:right">2020-10-01</td></tr>'
abstract += '<tr><td>End date:</td><td  style="text-align:right">2020-10-22</td></tr>'
abstract += '<tr><td>Video frames examined:</td><td style="text-align:right">174,944</td></tr>'
abstract += '<tr></tr>'
abstract += '<tr><td><b>V-cuts detected:</b></td><td style="text-align:right"><b>12,089</b></td></tr>'
abstract += '<tr></tr>'
abstract += '<tr><td>Coconut palm images:</td><td style="text-align:right">57,666</td></tr>'
abstract += '<tr><td>0 No damage:</td><td style="text-align:right">9,282</td></tr>'
abstract += '<tr><td>1 Light damage:</td><td style="text-align:right">38,944</td></tr>'
abstract += '<tr><td>2 Medium damage:</td><td style="text-align:right">7,458</td></tr>'
abstract += '<tr><td>3 High damage:</td><td style="text-align:right">1,063</td></tr>'
abstract += '<tr><td>4 Moribund or dead:</td><td style="text-align:right">519</td></tr>'
abstract += '<tr><td><b>Mean damage index:</td><td style="text-align:right"><b>1.025</b></td></tr>'
abstract += '<tr><td><b>Trees damaged:</td><td style="text-align:right"><b>83.9%</b></td></tr>'
abstract += '</table>'

# Load string with file contents
filepath = 'index.html'
with open(filepath, 'r') as f:
    s = f.read()

# Change fillOpacity for mean_damage_index symbology
s = re.sub(r"(feature\.properties\['mean_damage_index'\][\S\s]*?)(fillOpacity: 1)", r'\1fillOpacity: 0.75', s)

# Change width of the abstract box
s = re.sub(r"(\<style\>)", r"\1\n.abstractUncollapsed {max-width: 100%;}", s)

# Change abstract text
s = re.sub(r"(div.classList.add\(\"abstractUncollapsed\"\);\s+this._div.innerHTML = ')(.*)(';)", f'\\1{abstract}\\3', s)

# Disable hiding abstract: comment 2 lines and change another
s = re.sub(r"(this._div.setAttribute)", r'//\1', s)
s = re.sub(r"this.hide", r'this.show', s)

# write changes to new_abstract.html
filepath = filepath.replace('index', 'new_index')
with open(filepath, 'w') as f:
    f.write(s)
