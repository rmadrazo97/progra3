from flask import Flask

app=Flask('my app')
print("Hello From Docker")


@app.route("/")
def hello():
    return """
            <h1>Hola Mundo!</h1>
            <h2> Soy: Alejandro Madrazo </h2>
            <img src = "https://i.4pcdn.org/pol/1491357927577.png">

            """


app.run(host="0.0.0.0",port=5000)