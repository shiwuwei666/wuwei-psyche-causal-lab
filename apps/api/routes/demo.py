from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(tags=["demo"])


DEMO_HTML = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>Wuwei Psyche Causal Lab Demo</title>
</head>
<body>
  <h1>Wuwei Psyche Causal Lab</h1>
  <p>输入一段中文文本，看看简化版的心理因果分析结果。</p>
  <textarea id="input" rows="6" cols="60">最近工作压力很大，总觉得自己不够好。</textarea><br/>
  <button onclick="runAnalyze()">Analyze</button>
  <pre id="output"></pre>
  <script>
    async function runAnalyze() {
      const text = document.getElementById("input").value;
      const resp = await fetch("/v1/analyze", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text})
      });
      const data = await resp.json();
      document.getElementById("output").textContent = JSON.stringify(data, null, 2);
    }
  </script>
 </body>
 </html>
"""


@router.get("/demo", response_class=HTMLResponse)
def demo():
  return DEMO_HTML