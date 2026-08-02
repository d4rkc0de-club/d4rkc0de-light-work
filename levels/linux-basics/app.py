from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>Linux Basics</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:monospace;
}

body{
    background:#111;
    color:#eee;
    padding:16px;
}

main{
    max-width:420px;
    margin:auto;
}

h2{
    margin-bottom:6px;
}

p{
    color:#999;
    margin-bottom:18px;
    font-size:14px;
}

input{
    width:100%;
    padding:14px;
    font-size:16px;
    background:#000;
    color:#0f0;
    border:1px solid #333;
    outline:none;
    margin-bottom:10px;
}

button{
    width:100%;
    padding:14px;
    font-size:16px;
    background:#222;
    color:#fff;
    border:1px solid #333;
    cursor:pointer;
}

button:active{
    background:#333;
}

textarea{
    width:100%;
    height:320px;
    margin-top:14px;
    padding:14px;
    background:#000;
    color:#0f0;
    border:1px solid #333;
    resize:none;
    outline:none;
    font-size:14px;
}
</style>
</head>

<body>

<main>

<h2>Linux Basics</h2>
<p>Execute Linux commands to find both flags.</p>

<input
    id="cmd"
    placeholder="ls"
    autocomplete="off"
    spellcheck="false"
>

<button onclick="run()">Run</button>

<textarea id="out" readonly></textarea>

</main>

<script>
const cmd = document.getElementById("cmd");

cmd.addEventListener("keydown", function(e){
    if(e.key === "Enter"){
        run();
    }
});

async function run(){

    const command = cmd.value;

    const r = await fetch("/run",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            command:command
        })
    });

    const j = await r.json();

    document.getElementById("out").value = j.output;
}
</script>

</body>
</html>
"""

@app.route("/run", methods=["POST"])
def run():

    cmd = request.json.get("command","")

    try:

        result = subprocess.run(
            cmd,
            shell=True,
            cwd="/root",
            capture_output=True,
            text=True,
            timeout=3
        )

        output = (result.stdout + result.stderr).strip()

        if not output:
            output = "<no output on terminal>"

    except Exception as e:
        output = str(e)

    return jsonify({"output": output})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5021)