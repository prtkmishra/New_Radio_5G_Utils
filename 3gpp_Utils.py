import flask
from flask import request
from ra_rnti_Calculation.NR_5G_PRACH_RARNTI_Calculation import RaRntiCalculator as ra_calc
from PDSCH_RA_TimeDomain.NR_5G_PDSCH_Resource_Allocation_TimeDomain import TdResourceAllocation as td_calc
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/raRntiCalc', methods=['GET'])
def home():
    """ This constructor should be initialised with 
        arg1 : RAT_TYPE valid values: "FDD", "TDD" 
        arg2 : PRACH config index valid values: "0:255" 
        arg3 : TDD periodicity valid values: "please refer to 3GPP spec 38.213" 
        arg4 : In case user wants to give own file name, else leave blank" 
    """
    rat_type        = request.args.get('rat_type').upper()
    config_idx      = request.args.get('config_idx')
    tdd_periodicity = request.args.get('tdd_periodicity')
    ra_calc_obj     = ra_calc(rat_type,config_idx,tdd_periodicity)
    #ra_calc_obj.calc_valid_ra_slot()
    #return "<h1>3GPP Utilities</h1><p>This link provides utils for 3GPP based calculations.</p>"
    return ra_calc_obj.calc_valid_ra_slot()

@app.route('/tdRscCalc', methods=['GET'])
def td_rsc_calc():
    """ This constructor should be initialised with 
        arg1 : Valid values of PDSCH Start Symbols 
        arg2 : Valid values of PDSCH length in symbols" 
     """
    start_symbol    = request.args.get('start_symbol')
    length_value    = request.args.get('length_value')
    td_calc_obj = td_calc(start_symbol,length_value)
    return td_calc_obj.tdrscCalculator()




@app.route('/', methods=['GET'])
def usage():
    return "<h1>!!!!!!!!!Usage!!!!!!!!!!</h1><p>raRntiCalc?rat_type=FDD&config_idx=159&tdd_periodicity=4</p><p>tdRscCalc?start_symbol=2&length_value=3<p>"
app.run(host='0.0.0.0', port=5001)
