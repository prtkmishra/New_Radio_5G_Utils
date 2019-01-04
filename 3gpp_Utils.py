import flask
from flask import request
from ra_rnti_Calculation.NR_5G_PRACH_RARNTI_Calculation import RaRntiCalculator as ra_calc
from PDSCH_RA_TimeDomain.NR_5G_PDSCH_Resource_Allocation_TimeDomain import TdResourceAllocation as td_calc
from SUM_KR_LDPC.ComputeSumKrLdpc5G import ComputeSumKrLdpc as sumldpc

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


@app.route('/SumKrLdpc', methods=['GET'])
def sum_kr_ldpc():
    """ This constructor should be initialised with
        arg1 : Valid value of graph (1,2)
        arg2 : Valid value of TB SIZE in numeric
        arg3 : Valid value of number of HARQ bits
        arg4 : Valid value of Beta Offset
        arg5 : Valid value of  number of UL RBs
        arg6 : Valid value of length of ULSCH in Symbols
        arg7 : Valid value of Alpha
       """
    graph = int(request.args.get('graph'))
    TbSize = int(request.args.get('TbSize'))
    O_ack = int(request.args.get('O_ack'))
    Beta_Offset = int(request.args.get('Beta_Offset'))
    N_rb = int(request.args.get('N_rb'))
    N_Ul_Len = int(request.args.get('N_Ul_Len'))
    Alpha = int(request.args.get('Alpha'))
    sumldpc_obj = sumldpc(graph, TbSize, O_ack, Beta_Offset, N_rb, N_Ul_Len, Alpha)
    return sumldpc_obj.sum_kr()


@app.route('/', methods=['GET'])
def usage():
    return "<h1>!!!!!!!!!Usage!!!!!!!!!! \
           </h1><p>raRntiCalc?rat_type=FDD&config_idx=159&tdd_periodicity=4</p> \
           <p>tdRscCalc?start_symbol=2&length_value=3<p> \
            <p>SumKrLdpc?graph=1&TbSize=24&O_ack=2&Beta_Offset=4&N_rb=1&N_Ul_Len=10&Alpha=1<p>"
app.run(host='0.0.0.0', port=5001)
