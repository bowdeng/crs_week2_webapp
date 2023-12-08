from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def main():  # put application's code here
    return '''
    <form action="/echo_user_input" method="post">
        <input type="text" name="user_input"/>
        <input type="submit" value="Submit!"/>
    </form>
    '''


@app.route('/echo_user_input', methods=['POST'])
def echo_user_input():
    input_text = request.form.get('user_input', "")
    return "You entered " + input_text


if __name__ == '__main__':
    app.run()
