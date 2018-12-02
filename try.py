from flask import Flask, render_template, request
import csv
import dectree
# from pcagaussian import y_pred

# import pandas as pd
# import pcagaussian
# from pcagaussian import y_pred

app = Flask(__name__)


@app.route('/cp')
def index():
    return render_template('cp.html')


'''
@app.route('/cp', methods=['GET', 'POST'])
def cp():
    # value = request.args.get('key')
    if request.method == 'GET':
        result3 = request.form
        return render_template('cplung.html', result3=result3)
'''


@app.route('/level1eval', methods=['GET', 'POST'])
def level1eval():
    result = ""
    reslist = []
    x = -1
    if request.method == 'GET':
        if request.args.get('no') is not None:
            return render_template('level1result.html')

        # if request.args.get('age') is not None:
        #    result += request.args.get('age') + " "
        # else:
        #

        result += request.args.get('age') + " " + request.args.get('gender') + " " + request.args.get('smoke') + " " + request.args.get('obese') + " " + request.args.get('alcoholic') + " " + request.args.get('exercise') + " " + request.args.get('heredity') + " "
        if request.args.get('symp1') is not None:
            result += "1" + " "
        if request.args.get('symp2') is not None:
            result += "2" + " "
        if request.args.get('symp3') is not None:
            result += "4" + " "
        if request.args.get('symp4') is not None:
            result += "3" + " "
        if request.args.get('symp5') is not None:
            result += "5" + " "
        if request.args.get('symp6') is not None:
            result += "6" + " "
        if request.args.get('symp7') is not None:
            result += "7" + " "
        if request.args.get('symp8') is not None:
            result += "8" + " "
        if request.args.get('symp9') is not None:
            result += "9" + " "
        if request.args.get('symp10') is not None:
            result += "10" + " "
        if request.args.get('symp11') is not None:
            result += "27" + " "
        if request.args.get('symp12') is not None:
            result += "13" + " "
        if request.args.get('symp13') is not None:
            result += "28" + " "
        if request.args.get('symp14') is not None:
            result += "29" + " "
        if request.args.get('symp15') is not None:
            result += "30" + " "
        if request.args.get('symp16') is not None:
            result += "26" + " "
        if request.args.get('symp17') is not None:
            result += "15" + " "
        if request.args.get('symp18') is not None:
            result += "16" + " "
        if request.args.get('symp19') is not None:
            result += "17" + " "
        if request.args.get('symp20') is not None:
            result += "18" + " "
        if request.args.get('symp21') is not None:
            result += "19" + " "
        if request.args.get('symp22') is not None:
            result += "20" + " "

        #result += "-1"+" "+"-1"+" "+"-1"+" "+"-1"+" "+"-1"

        reslist = result.split()
        print(reslist)
        u = "999"
        while len(reslist) != 18:
            reslist.append(u)
        print("before inserting to excel",reslist)
        with open('newdata.csv', 'a', newline='') as out:
            w = csv.writer(out)
            w.writerow(reslist)
        print(w)
        print("AFTER INSERTING TO EXCEL",reslist)
        print()
        x = dectree.dt()
        print(x)

        if x == 0:
            return render_template('cpstom.html')

        if x == 1:
            return render_template('cporal.html')

        if x == 2:
            return render_template('cplung.html')

        if x == 3:
            return render_template('level1result.html')

        #if x == -1:
        #    return render_template('level1result.html')
    return render_template('defaultpg.html')

    # result = result.append(request.args.get('age'))
    # result = result.append(request.args.get('gender'))

    # with open('output.csv', 'a', newline='') as out:
    #     w = csv.writer(out)
    #     w.writerow(reslist)

    # pcaoutput = y_pred
    # if pcaoutput == 1:
    # return render_template('level1result.html')

    # return render_template('level1eval.html', reslist=reslist)

    # return render_template('level1result.html', output=output)

    # df = pd.DataFrame(data=result, index=[0])
    # df = (df.T)
    # df.to_excel('dict1.xlsx')

    # result = request.args.get('age')    # request.query_string    # request.form
    # do stuff when the form is submitted

    # redirect to end the POST handling
    # the redirect can be to the same route or somewhere else
    # return redirect(url_for('cp'))
    # return render_template('cpstom.html')

    # return render_template('cplung.html', result=result)

    # show the form, it wasn't submitted
    # return render_template('cplung.html')


@app.route('/cplung', methods=['GET', 'POST'])
def cplung():
    return render_template('cplung.html')


@app.route('/cplungeval', methods=['GET', 'POST'])
def cplungeval():

    lprob = 0
    resultl = ""
    lcount = 0
    # if request.method == 'GET':

    if request.args.get('sympl1') is None:
        lcount += 0
    else:
        lcount += 1
        # resultl += request.args.get('symp1')+" "
    if request.args.get('sympl2') is None:
        lcount += 0
    else:
        lcount += 1
        # resultl += request.args.get('symp2')+" "
    if request.args.get('sympl3') is None:
        lcount += 0
    else:
        lcount += 1
        # resultl += request.args.get('symp3')+" "
    if request.args.get('sympl4') is None:
        lcount += 0
    else:
        lcount += 1
        # resultl += request.args.get('symp4')+" "
    if request.args.get('sympl5') is None:
        lcount += 0
    else:
        lcount += 1
        # resultl += request.args.get('symp5')+" "

    lprob = (lcount/5)*100
    print(lprob)

    return render_template('cplungeval.html', lprob=lprob)

    # return render_template('level1result.html', output=output)

    # df = pd.DataFrame(data=result, index=[0])
    # df = (df.T)
    # df.to_excel('dict1.xlsx')

    # result = request.args.get('age')    # request.query_string    # request.form
    # do stuff when the form is submitted

    # redirect to end the POST handling
    # the redirect can be to the same route or somewhere else
    # return redirect(url_for('cp'))
    # return render_template('cpstom.html')

    # return render_template('cplung.html', result=result)
    # show the form, it wasn't submitted
    # return render_template('cplung.html')


@app.route('/cpstom', methods=['GET', 'POST'])
def cpstom():
    return render_template('cpstom.html')


@app.route('/cpstomeval', methods=['GET', 'POST'])
def cpstomeval():
    scount = 0
    # sprob = 0
    if request.args.get('symps1') is None:
        scount += 0
    else:
        scount += 1
    if request.args.get('symps2') is None:
        scount += 0
    else:
        scount += 1
    if request.args.get('symps3') is None:
        scount += 0
    else:
        scount += 1
    if request.args.get('symps4') is None:
        scount += 0
    else:
        scount += 1

    sprob = (scount/4)*100
    print(sprob)
    return render_template('cpstomeval.html', sprob=sprob)

    # if request.method == 'POST':
    #    result1 = request.form
    # do stuff when the form is submitted

    # redirect to end the POST handling
    # the redirect can be to the same route or somewhere else
    # return redirect(url_for('cp'))
    # return render_template('cpstom.html')


@app.route('/cporal', methods=['GET', 'POST'])
def cporal():
    return render_template('cporal.html')


@app.route('/cporaleval', methods=['GET', 'POST'])
def cporaleval():
    ocount = 0
    oprob = 0
    if request.args.get('sympo1') is None:
        ocount += 0
    else:
        ocount += 1
    if request.args.get('sympo2') is None:
        ocount += 0
    else:
        ocount += 1
    if request.args.get('sympo3') is None:
        ocount += 0
    else:
        ocount += 1
    if request.args.get('sympo4') is None:
        ocount += 0
    else:
        ocount += 1
    if request.args.get('sympo5') is None:
        ocount += 0
    else:
        ocount += 1

    oprob = (ocount/5)*100
    print(oprob)
    return render_template('cporaleval.html', oprob=oprob)

    # if request.method == 'POST':
    #   result2 = request.form
    # do stuff when the form is submitted

    # redirect to end the POST handling
    # the redirect can be to the same route or somewhere else
    # return redirect(url_for('cp'))
    # return render_template('cporal.html', result2=result2)

    # show the form, it wasn't submitted
    # return render_template('cporal.html')


'''
#@app.route('/collection', methods=['GET', 'POST'])
def collection():
    lprob = 0
    resultl = ""
    lcount = 0
    # if request.method == 'GET':

    if request.args.get('sympl1') is None:
        lcount += 0
    else:
        lcount += 1
        # resultl += request.args.get('symp1')+" "
    if request.args.get('sympl2') is None:
        lcount += 0
    else:
        lcount += 1
        # resultl += request.args.get('symp2')+" "
    if request.args.get('sympl3') is None:
        lcount += 0
    else:
        lcount += 1
        # resultl += request.args.get('symp3')+" "
    if request.args.get('sympl4') is None:
        lcount += 0
    else:
        lcount += 1
        # resultl += request.args.get('symp4')+" "
    if request.args.get('sympl5') is None:
        lcount += 0
    else:
        lcount += 1
        # resultl += request.args.get('symp5')+" "

    lprob = (lcount / 5)*10
    print(lprob)

    return render_template('collection.html', lprob=lprob)
'''


@app.route('/mainpg', methods=['GET', 'POST'])
def mainpg():
    return render_template('mainpg.html')


@app.route('/index', methods=['GET', 'POST'])
def ind():
    return render_template('index.html')


@app.route('/level1result', methods=['GET', 'POST'])
def l1r():
    return render_template('level1result.html')


if __name__ == "__main__":
    app.run(debug=True)
