from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # HTML com CSS embutido para a página
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Feliz Dia das Mulheres!</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-color: #ffe6f2;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                text-align: center;
                overflow: hidden;
            }
            .container {
                max-width: 800px;
                padding: 30px;
                background-color: white;
                border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                position: relative;
                z-index: 1;
            }
            h1 {
                color: #d81b60;
                font-size: 2.5em;
                margin-bottom: 20px;
            }
            p {
                color: #555;
                font-size: 1.2em;
                line-height: 1.6;
                margin-bottom: 20px;
            }
            .heart {
                font-size: 1.5em;
                color: #d81b60;
            }
            .flower {
                position: absolute;
                opacity: 0.6;
                animation: float 8s infinite ease-in-out;
            }
            @keyframes float {
                0%, 100% { transform: translateY(0) rotate(0deg); }
                50% { transform: translateY(-20px) rotate(10deg); }
            }
            .signature {
                font-style: italic;
                margin-top: 30px;
                font-size: 1.1em;
                color: #888;
            }
        </style>
    </head>
    <body>
        <div class="flower" style="top: 10%; left: 10%;">🌸</div>
        <div class="flower" style="top: 20%; left: 80%;">🌷</div>
        <div class="flower" style="top: 70%; left: 15%;">🌹</div>
        <div class="flower" style="top: 60%; left: 85%;">🌺</div>
        <div class="flower" style="top: 80%; left: 50%;">🌻</div>
        
        <div class="container">
            <h1>Feliz Dia Internacional da Mulher!</h1>
            <p>
                Para celebrar a força, coragem e beleza que você traz ao mundo todos os dias.
                Sua determinação inspira, seu sorriso ilumina, e sua presença faz toda a diferença.
            </p>
            <p>
                Que este dia seja apenas um lembrete do quanto você é especial e admirável todos os dias do ano.
            </p>
            <p class="heart">❤️</p>
            <div class="signature"><h1>Com carinho, J.Victor</h1></div>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)