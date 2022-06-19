from browser import document, html

calc = html.TABLE()

calc <= html.TR(html.TH(html.DIV("0", id="result"), colspan=3) + html.TD("C"))

lines = ["789/", "456*", "123-", "0.=+"]
calc <= (html.TR(html.TD(x) for x in line) for line in lines)

"""
<table>
<tr>
  <th id="result" colspan="3">0</th>
  <td>C</td>
</tr>
<tr>
  <td>7</td>
  <td>8</td>
  <td>9</td>
  <td>/</td>
</tr>
<tr>
  <td>4</td>
  <td>5</td>
  <td>6</td>
  <td>*</td>
</tr>
<tr>
  <td>1</td>
  <td>2</td>
  <td>3</td>
  <td>-</td>
</tr>
<tr>
  <td>0</td>
  <td>.</td>
  <td>=</td>
  <td>+</td>
</tr>
</table>
"""

document["calc"] <= calc

result = document["result"]

def action(event):
    element = event.target
    value = element.text
    if value == "C":
        result.text = "0"
    elif value == "=":
        try:
            result.text = eval(result.text)
        except:
            result.text = "error"
    elif result.text in ["0", "error"]:
        result.text = value
    else:
        result.text += value

for button in document.select("td"):
    button.bind("click", action)
