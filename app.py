from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Zopone - Interfone Digital</title>

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        body {
            background: #0b0b0b;
            color: white;
            min-height: 100vh;
            transition: 0.3s;
        }

        body.claro {
            background: #f4f4f4;
            color: #111;
        }

        header {
            padding: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #00c853;
        }

        .logo {
            color: #00c853;
            font-size: 30px;
            font-weight: bold;
        }

        .subtitulo {
            font-size: 13px;
            opacity: 0.7;
            margin-top: 4px;
        }

        button {
            cursor: pointer;
            border: none;
        }

        #tema {
            background: #00c853;
            color: #000;
            padding: 10px 15px;
            border-radius: 8px;
            font-weight: bold;
        }

        main {
            max-width: 1000px;
            margin: auto;
            padding: 30px 20px;
        }

        h1 {
            text-align: center;
            margin-bottom: 25px;
            color: #00c853;
        }

        .andares {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            max-width: 650px;
            margin: auto;
        }

        .andar,
        .portaria {
            padding: 18px;
            border-radius: 10px;
            background: #181818;
            color: white;
            border: 1px solid #00c853;
            font-size: 16px;
            font-weight: bold;
            transition: 0.2s;
        }

        body.claro .andar {
            background: white;
            color: #111;
        }

        .andar:hover,
        .portaria:hover {
            background: #00c853;
            color: black;
            transform: translateY(-2px);
        }

        .portaria {
            grid-column: span 2;
            background: #00c853;
            color: black;
        }

        .salas {
            display: none;
        }

        .salas.ativa {
            display: block;
        }

        .voltar {
            display: block;
            margin: 0 auto 20px auto;
            padding: 10px 18px;
            border-radius: 8px;
            background: #333;
            color: white;
        }

        body.claro .voltar {
            background: #ddd;
            color: #111;
        }

        .titulo-andar {
            text-align: center;
            color: #00c853;
            margin-bottom: 20px;
        }

        .grid-salas {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
        }

        .sala {
            background: #181818;
            border: 1px solid #333;
            border-radius: 12px;
            padding: 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        body.claro .sala {
            background: white;
            border: 1px solid #ddd;
        }

        .nome-sala {
            font-weight: bold;
        }

        .status {
            margin-top: 6px;
            font-size: 12px;
            font-weight: bold;
        }

        .online {
            color: #00c853;
        }

        .offline {
            color: #ff3333;
        }

        .chamar {
            background: #00c853;
            color: black;
            padding: 10px 13px;
            border-radius: 8px;
            font-size: 18px;
        }

        .chamar:hover {
            transform: scale(1.08);
        }

        #mensagem {
            text-align: center;
            margin-top: 25px;
            min-height: 25px;
            color: #00c853;
            font-weight: bold;
        }

        @media (max-width: 600px) {

            header {
                flex-direction: column;
                gap: 15px;
                text-align: center;
            }

            .andares {
                grid-template-columns: 1fr;
            }

            .portaria {
                grid-column: span 1;
            }

            .grid-salas {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>

<body>

<header>

    <div>
        <div class="logo">ZOPONE</div>
        <div class="subtitulo">INTERFONE DIGITAL</div>
    </div>

    <button id="tema" onclick="trocarTema()">
        ☀️ MODO CLARO
    </button>

</header>


<main>

    <!-- MENU DOS ANDARES -->

    <section id="menu">

        <h1>SELECIONE O ANDAR</h1>

        <div class="andares">

            <button class="portaria" onclick="mostrarPortaria()">
                🏢 PORTARIA
            </button>

            <button class="andar" onclick="mostrarAndar(1)">1º ANDAR</button>
            <button class="andar" onclick="mostrarAndar(2)">2º ANDAR</button>

            <button class="andar" onclick="mostrarAndar(3)">3º ANDAR</button>
            <button class="andar" onclick="mostrarAndar(4)">4º ANDAR</button>

            <button class="andar" onclick="mostrarAndar(5)">5º ANDAR</button>
            <button class="andar" onclick="mostrarAndar(6)">6º ANDAR</button>

            <button class="andar" onclick="mostrarAndar(7)">7º ANDAR</button>
            <button class="andar" onclick="mostrarAndar(8)">8º ANDAR</button>

            <button class="andar" onclick="mostrarAndar(9)">9º ANDAR</button>
            <button class="andar" onclick="mostrarAndar(10)">10º ANDAR</button>

        </div>

    </section>


    <!-- SALAS -->

    <section id="salas" class="salas">

        <button class="voltar" onclick="voltar()">
            ← VOLTAR
        </button>

        <h1 class="titulo-andar" id="tituloAndar"></h1>

        <div class="grid-salas" id="listaSalas"></div>

    </section>


    <div id="mensagem"></div>

</main>


<script>

    // ==========================================
    // SOM DO INTERFONE
    // ==========================================

    function tocarSom() {

        const audioContext =
            new (window.AudioContext || window.webkitAudioContext)();

        function toque(frequencia, inicio) {

            const oscilador =
                audioContext.createOscillator();

            const ganho =
                audioContext.createGain();

            oscilador.frequency.value = frequencia;

            oscilador.type = "sine";

            oscilador.connect(ganho);

            ganho.connect(audioContext.destination);

            ganho.gain.setValueAtTime(
                0.0001,
                audioContext.currentTime + inicio
            );

            ganho.gain.exponentialRampToValueAtTime(
                0.25,
                audioContext.currentTime + inicio + 0.02
            );

            ganho.gain.exponentialRampToValueAtTime(
                0.0001,
                audioContext.currentTime + inicio + 0.35
            );

            oscilador.start(
                audioContext.currentTime + inicio
            );

            oscilador.stop(
                audioContext.currentTime + inicio + 0.4
            );
        }

        toque(900, 0);
        toque(1200, 0.45);
    }


    // ==========================================
    // MOSTRAR ANDAR
    // ==========================================

    function mostrarAndar(andar) {

        document.getElementById("menu").style.display = "none";

        document.getElementById("salas")
            .classList.add("ativa");

        document.getElementById("tituloAndar")
            .innerText = andar + "º ANDAR";

        const lista =
            document.getElementById("listaSalas");

        lista.innerHTML = "";

        for (let sala = 1; sala <= 10; sala++) {

            // Alguns exemplos online/offline
            let online =
                ((andar + sala) % 4 !== 0);

            let status =
                online ? "ONLINE" : "OFFLINE";

            let classe =
                online ? "online" : "offline";

            let botao =
                online
                ? `<button class="chamar"
                    onclick="chamarSala(${andar}, ${sala})">
                    📞
                   </button>`
                : `<button class="chamar"
                    onclick="salaOffline()">
                    📞
                   </button>`;

            lista.innerHTML += `

                <div class="sala">

                    <div>

                        <div class="nome-sala">
                            🚪 Sala ${sala}
                        </div>

                        <div class="status ${classe}">
                            ● ${status}
                        </div>

                    </div>

                    ${botao}

                </div>
            `;
        }
    }


    // ==========================================
    // CHAMAR SALA
    // ==========================================

    function chamarSala(andar, sala) {

        tocarSom();

        document.getElementById("mensagem")
            .innerText =
            "📞 Chamando Sala " +
            sala +
            " - " +
            andar +
            "º andar...";
    }


    // ==========================================
    // SALA OFFLINE
    // ==========================================

    function salaOffline() {

        document.getElementById("mensagem")
            .innerText =
            "🔴 Esta sala está OFFLINE.";
    }


    // ==========================================
    // PORTARIA
    // ==========================================

    function mostrarPortaria() {

        tocarSom();

        document.getElementById("menu").style.display =
            "none";

        document.getElementById("salas")
            .classList.add("ativa");

        document.getElementById("tituloAndar")
            .innerText = "🏢 PORTARIA";

        document.getElementById("listaSalas").innerHTML = `

            <div class="sala">

                <div>

                    <div class="nome-sala">
                        PORTARIA
                    </div>

                    <div class="status online">
                        ● ONLINE
                    </div>

                </div>

                <button class="chamar"
                    onclick="chamarSala('Portaria', '')">
                    📞
                </button>

            </div>

        `;
    }


    // ==========================================
    // VOLTAR
    // ==========================================

    function voltar() {

        document.getElementById("salas")
            .classList.remove("ativa");

        document.getElementById("menu").style.display =
            "block";

        document.getElementById("mensagem")
            .innerText = "";
    }


    // ==========================================
    // MODO CLARO / ESCURO
    // ==========================================

    function trocarTema() {

        document.body.classList.toggle("claro");

        const botao =
            document.getElementById("tema");

        if (document.body.classList.contains("claro")) {

            botao.innerText =
                "🌙 MODO ESCURO";

        } else {

            botao.innerText =
                "☀️ MODO CLARO";
        }
    }

</script>

</body>
</html>
"""


@app.route("/")
def inicio():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(debug=True)

