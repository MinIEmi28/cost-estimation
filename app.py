from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Load the Excel data
df = pd.read_excel('cost_data.xlsx')

# Extract data for dropdowns and units
materials_data = df[['Type', 'Group', 'Unit']].to_dict(orient='records')

# Extract data for dropdowns
# copper_types = df[df['Group'] == 1]['Type'].tolist()
# insulation_materials = df[df['Group'] == 2]['Type'].tolist()
# reactor_materials =df[df['Group'] == 3]['Type'].tolist()
# core_steel_types = df[df['Group'] == 4]['Type'].tolist()
# terminal_gear =df[df['Group'] == 5]['Type'].tolist()
# tca_control =df[df['Group'] == 6]['Type'].tolist()
# _g7 = df[df['Group'] == 7]['Type'].tolist()
# _g8 = df[df['Group'] == 8]['Type'].tolist()
# _g9 = df[df['Group'] == 9]['Type'].tolist()
# _g10 = df[df['Group'] == 10]['Type'].tolist()
# cooler_assy = df[df['Group'] == 14]['Type'].tolist()
# fabrication = df[df['Group'] == 16]['Type'].tolist()
# _g17 = df[df['Group'] == 17]['Type'].tolist()
# _g18 = df[df['Group'] == 18]['Type'].tolist()
# _g19 = df[df['Group'] == 19]['Type'].tolist()
# _g20 = df[df['Group'] == 20]['Type'].tolist()
# _g21 = df[df['Group'] == 21]['Type'].tolist()

# Extract other materials similarly...

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/materials', methods=['POST'])
def materials():
    kva = request.form['kva']
    primary_voltage = request.form['primary_voltage']
    secondary_voltage = request.form['secondary_voltage']
    phase = request.form['phase']
    # return render_template('materials.html', copper_types=copper_types, core_steel_types=core_steel_types, insulation_materials=insulation_materials, reactor_materials=reactor_materials, terminal_gear=terminal_gear, tca_control=tca_control, _g7=_g7, _g8=_g8, _g9=_g9, _g10=_g10, cooler_assy=cooler_assy, fabrication=fabrication, _g17=_g17, _g18=_g18, _g19=_g19, _g20=_g20, _g21=_g21, )
    return render_template('materials.html', materials_data=materials_data )


@app.route('/result', methods=['POST'])
def result():
    # Get material data from form
    copper_type = request.form['copper_type']
    copper_amount = float(request.form['copper_amount'])
    insulation = request.form.getlist('insulation')
    reactor = request.form.getlist('reactor_materials')
    steel_type = request.form['steel_type']
    steel_amount = float(request.form['steel_amount'])
    terminal_gear = request.form.getlist('terminal_gear')
    tca_control = request.form.getlist('tca_control')
    _g7 = request.form.getlist('_g7')
    _g8 = request.form.getlist('_g8')
    _g9 = request.form.getlist('_g9')
    _g10 = request.form.getlist('_g10')
    cooler_assy = request.form.getlist('cooler_assy')
    fabrication = request.form.getlist('fabrication')
    _g17 = request.form.getlist('_g17')
    _g18 = request.form.getlist('_g18')
    _g19 = request.form.getlist('_g19')
    _g20 = request.form.getlist('_g20')
    _g21 = request.form.getlist('_g21')

    # Calculate estimated cost
    estimated_cost = 0

    copper_cost = df[(df['Group'] == 1) & (df['Type'] == copper_type)]['Price_per_Unit'].values[0] * copper_amount
    estimated_cost += copper_cost

    for material in insulation:
        if material:
            insulation_cost = df[(df['Group'] == 2) & (df['Type'] == material)]['Price_per_Unit'].values[0] * float(request.form[f'insulation[{material}]'])
            estimated_cost += insulation_cost

    
    for material in reactor:
        if material:
            reactor_cost = df[(df['Group'] == 3) & (df['Type'] == material)]['Price_per_Unit'].values[0] * float(request.form[f'reactor[{material}]'])
            estimated_cost += reactor_cost

    steel_cost = df[(df['Group'] == 4) & (df['Type'] == steel_type)]['Price_per_Unit'].values[0] * steel_amount
    estimated_cost += steel_cost

    for material in terminal_gear:
        if material:
            gear_cost = df[(df['Group'] == 5) & (df['Type'] == material)]['Price_per_Unit'].values[0] * float(request.form[f'terminal_gear[{material}]'])
            estimated_cost += gear_cost

    for material in tca_control:
        if material:
            tca_control_cost = df[(df['Group'] == 6) & (df['Type'] == material)]['Price_per_Unit'].values[0] * float(request.form[f'tca_control[{material}]'])
            estimated_cost += tca_control_cost

    for material in _g7:
        if material:
            _g7_cost = df[(df['Group'] == 7) & (df['Type'] == material)]['Price_per_Unit'].values[0] * float(request.form[f'_g7[{material}]'])
            estimated_cost += _g7_cost
    for material in _g8:
        if material:
            _g8_cost = df[(df['Group'] == 8) & (df['Type'] == material)]['Price_per_Unit'].values[0] * float(request.form[f'_g8[{material}]'])
            estimated_cost += _g8_cost
    for material in _g9:
        if material:
            _g9_cost = df[(df['Group'] == 9) & (df['Type'] == material)]['Price_per_Unit'].values[0] * float(request.form[f'_g9[{material}]'])
            estimated_cost += _g9_cost
    for material in _g10:
        if material:
            _g10_cost = df[(df['Group'] == 10) & (df['Type'] == material)]['Price_per_Unit'].values[0] * float(request.form[f'_g10[{material}]'])
            estimated_cost += _g10_cost       
    for material in cooler_assy:
        if material:
            cooler_cost = df[(df['Group'] == 14) & (df['Type'] == material)]['Price_per_Unit'].values[0] * float(request.form[f'cooler_assy[{material}]'])
            estimated_cost += cooler_cost
    for material in fabrication:
        if material:
            fabrication_cost = df[(df['Group'] == 16) & (df['Type'] == material)]['Price_per_Unit'].values[0] * float(request.form[f'fabrication[{material}]'])
            estimated_cost += fabrication_cost
    for material in _g17:
        if material:
            _g17_cost = df[(df['Group'] == 17) & (df['Type'] == material)]['Price_per_Unit'].values[0] * float(request.form[f'_g17[{material}]'])
            estimated_cost += _g17_cost 
    for material in _g18:
        if material:
            _g18_cost = df[(df['Group'] == 18) & (df['Type'] == material)]['Price_per_Unit'].values[0] * float(request.form[f'_g18[{material}]'])
            estimated_cost += _g18_cost 
    for material in _g19:
        if material:
            _g19_cost = df[(df['Group'] == 19) & (df['Type'] == material)]['Price_per_Unit'].values[0] * float(request.form[f'_g19[{material}]'])
            estimated_cost += _g19_cost 
    for material in _g20:
        if material:
            _g20_cost = df[(df['Group'] == 20) & (df['Type'] == material)]['Price_per_Unit'].values[0] * float(request.form[f'_g20[{material}]'])
            estimated_cost += _g20_cost     
    for material in _g21:
        if material:
            _g21_cost = df[(df['Group'] == 21) & (df['Type'] == material)]['Price_per_Unit'].values[0] * float(request.form[f'_g21[{material}]'])
            estimated_cost += _g21_cost            
    return render_template('result.html', estimated_cost=estimated_cost)


if __name__ == '__main__':
    app.run(debug=True)
