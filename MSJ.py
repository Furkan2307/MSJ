from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Mesajları depolamak için bir liste
messages = []

# Ana sayfa (Mesajlaşma ekranı)
@app.route("/")
def index():
    return render_template("chat.html")

# Mesaj gönderme rotası
@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.get_json()  # JSON formatında gelen veriyi al
    message = data.get("message")  # Mesaj içeriğini al
    messages.append(message)  # Mesajı listeye ekle
    return jsonify({"message": message})  # Mesajı geri döndür

if __name__ == "__main__":
    
    app.run(host="0.0.0.0")
