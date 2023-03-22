import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
import streamlit as st


# add title to the page
st.title("Airports Cost Optimization Dashboard")

# set up sliders
st.sidebar.header('Current State')
number_of_vehicles = st.sidebar.slider('Number of Vehicles', 0, 100, 10, key = 'number_of_vehicles')
number_of_vehicles_text =st.sidebar.text_input('Number of Vehicles', number_of_vehicles)

fuel_efficiency = st.sidebar.slider('Fuel Efficiency (kmpl)', 0, 100, 10, key = 'fuel_efficiency')
fuel_efficiency_text = st.sidebar.text_input('Fuel Efficiency (kmpl)', fuel_efficiency)

cost_of_fuel = st.sidebar.slider('Cost of Fuel (in ₹)', 0, 100, 10, key = 'cost_of_fuel')
cost_of_fuel_text = st.sidebar.text_input('Cost of Fuel (in ₹)', cost_of_fuel)

idling_time = st.sidebar.slider('Idling Time (minutes)', 0, 100, 10, key = 'idling_time')
idling_time_text = st.sidebar.text_input('Idling Time (in minutes)', idling_time)

number_of_aircrafts_attended= st.sidebar.slider('Number of aircrafts attended', 0, 100, 10, key = 'number_of_aircrafts_attended')
number_of_aircrafts_attended_text = st.sidebar.text_input('Number of aircrafts attended', number_of_aircrafts_attended)

st.sidebar.header('Optimization')
opt_number_of_vehicles = st.sidebar.slider('Number of Vehicles', 0, 100, 0, key = 'opt_number_of_vehicles')
opt_number_of_vehicles_text =st.sidebar.text_input('Number of Vehicles', opt_number_of_vehicles, key = "opt_number_of_vehicles_text")

opt_fuel_efficiency = st.sidebar.slider('Fuel Efficiency (kmpl)', 0, 100, 10, key = 'opt_fuel_efficiency')
opt_fuel_efficiency_text = st.sidebar.text_input('Fuel Efficiency (kmpl)', opt_fuel_efficiency, key =" opt_fuel_efficiency_text")

opt_cost_of_fuel = st.sidebar.slider('Cost of Fuel (in ₹)', 0, 100, 0, key = 'opt_cost_of_fuel')
opt_cost_of_fuel_text = st.sidebar.text_input('Cost of Fuel (in ₹)', opt_cost_of_fuel, key = "opt_cost_of_fuel_text")

opt_idling_time = st.sidebar.slider('Idling Time (in minutes)', 0, 100, 0, key = 'opt_idling_time')
opt_idling_time_text = st.sidebar.text_input('Idling Time (in minutes)', opt_idling_time, key = "opt_idling_time_text")

opt_number_of_aircrafts_attended= st.sidebar.slider('Number of aircrafts attended', 0, 100, 0, key = 'opt_number_of_aircrafts_attended')
opt_number_of_aircrafts_attended_text = st.sidebar.text_input('Number of aircrafts attended', opt_number_of_aircrafts_attended,key = "opt_number_of_aircrafts_attended_text")

# convert text input to integers
number_of_vehicles = int(number_of_vehicles_text) if number_of_vehicles_text else number_of_vehicles
fuel_efficiency = int(fuel_efficiency_text) if fuel_efficiency_text else fuel_efficiency
cost_of_fuel = int(cost_of_fuel_text) if cost_of_fuel_text else cost_of_fuel
idling_time = int(idling_time_text) if idling_time_text else idling_time
number_of_aircrafts_attended = int(number_of_aircrafts_attended_text) if number_of_aircrafts_attended_text else number_of_aircrafts_attended

opt_number_of_vehicles = int(opt_number_of_vehicles_text) if opt_number_of_vehicles_text else opt_number_of_vehicles
opt_fuel_efficiency = int(opt_fuel_efficiency_text) if opt_fuel_efficiency_text else opt_fuel_efficiency
opt_cost_of_fuel = int(opt_cost_of_fuel_text) if opt_cost_of_fuel_text else opt_cost_of_fuel
opt_idling_time = int(opt_idling_time_text) if opt_idling_time_text else opt_idling_time
opt_number_of_aircrafts_attended = int(opt_number_of_aircrafts_attended_text) if opt_number_of_aircrafts_attended_text else opt_number_of_aircrafts_attended



# calculate costs
if fuel_efficiency == 0:
    st.error('Fuel efficiency cannot be 0.')
    cur_cost = 0
else:
    cur_cost = number_of_vehicles*(10/fuel_efficiency)*cost_of_fuel*(idling_time/60)*number_of_aircrafts_attended*12

if opt_fuel_efficiency == 0:
    st.error('Fuel efficiency cannot be 0.')
    opt_cost = 0
else:
    opt_cost = opt_number_of_vehicles*(10/opt_fuel_efficiency)*opt_cost_of_fuel*(opt_idling_time/60)*opt_number_of_aircrafts_attended*12

#calculate net profit
net_profit = cur_cost - opt_cost

#create chart
fig = make_subplots(rows=1, cols=2)

fig.add_trace(
    go.Bar(x=['Current Cost', 'Optimized Cost'], y=[cur_cost, opt_cost], marker_color=['red', 'green'],text=[f'₹{int(cur_cost)}',f'₹{int(opt_cost)}'], textposition= 'auto'),
    row=1, col=1
)

# create collapsible button for net profit bar
if st.button("Toggle Net Profit Bar"):
    show_net_profit = not st.session_state.get("show_net_profit", False)
    st.session_state["show_net_profit"] = show_net_profit
else:
    show_net_profit = st.session_state.get("show_net_profit", False)

# add net profit bar
if show_net_profit:
    fig.add_trace(
        go.Bar(x=['Net Profit'], y=[net_profit], marker_color=['blue'],text = [f'₹{int(net_profit)}'],textposition='auto'),
        row=1, col=2
    )

fig.update_layout(height=400, width=800, title_text="Per Annum Cost Comparison ", showlegend=False)

st.plotly_chart(fig)
