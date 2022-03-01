
from http.client import NOT_ACCEPTABLE
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def display():
    return render_template('index.html')

# route to compute payroll
@app.route('/compute_payroll', methods=['GET', 'POST'])
def compute_payroll():
    if request.method == 'POST':
        rate = request.form['rate']
        hours = request.form['hour']
        allowance = request.form['allowance']
        sss = request.form['sss']
        pag_ibig = request.form['pag_ibig']
        philhealth = request.form['philhealth']

    #    computations for Gross Pay
        gross_pay = (float(rate) * float(hours)) + float(allowance)
        deductions = (float(sss) + float(pag_ibig) + float(philhealth))
        net_pay = gross_pay - deductions

        # NOTE: Always return String not any type but string
        return f""" <h2>Gross Pay: {gross_pay} </h2> 
        <h2> Deductions: {deductions}</h2>
        <h2>Net Pay: {net_pay}</h2>"""


if __name__ == "__main__":
    app.run()