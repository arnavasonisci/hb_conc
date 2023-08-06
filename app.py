from mastercsv import *

# incorporate the data
df, avg_df = makeMaster()

print(df.shape)
# initialize the app
app = Dash(__name__)

# assigning data type to the columns
def table_type(df_column):
    if sys.version_info < (3, 0):
        return 'any'
    
    if isinstance(df_column.dtype, pd.DatetimeTZDtype):
        return 'datetime',
    elif (isinstance(df_column.dtype, pd.StringDtype) or
            isinstance(df_column.dtype, pd.BooleanDtype) or
            isinstance(df_column.dtype, pd.CategoricalDtype) or
            isinstance(df_column.dtype, pd.PeriodDtype)):
        return 'text'
    elif (isinstance(df_column.dtype, pd.SparseDtype) or
            isinstance(df_column.dtype, pd.IntervalDtype) or
            isinstance(df_column.dtype, pd.Int8Dtype) or
            isinstance(df_column.dtype, pd.Int16Dtype) or
            isinstance(df_column.dtype, pd.Int32Dtype) or
            isinstance(df_column.dtype, pd.Int64Dtype)):
        return 'numeric'
    else:
        return 'any'


# app layout
app.layout = html.Div([
    html.H2(children='Date Folder Path'),
    html.Div(
        dcc.Input(
            id="input_{}".format("text"),
            type="text",
            placeholder="input date folder path"
        )
    ),

    html.H2(children='App with data'),
    dash_table.DataTable(
        columns=[
            {'name': i, 'id': i, 'type': table_type(df[i])} for i in df.columns
        ],
        data=df.to_dict('records'),
        filter_action = 'native',
        page_size=10 
    ),

    html.H2(children='Average data'),
    dash_table.DataTable(
        columns=[
            {'name': i, 'id': i, 'type': table_type(avg_df[i])} for i in avg_df.columns
        ],
        data=avg_df.to_dict('records'),
        page_size = 5 
    ),
    # channel subplots
    html.H2(children='Peak Values'),
    dcc.Graph(figure=make_subplots(rows=3, cols=3,
                                   subplot_titles=['Blue Channel Peaks',
                                                   'Green Channel Peaks',
                                                   'Red Channel Peaks',
                                                   'Hue Channel Peaks',
                                                   'Saturation Channel Peaks',
                                                   'Value Channel Peaks',
                                                   'Luminance Channel Peaks',
                                                   'Red-Green Channel Peaks',
                                                   'Yellow-Blue Channel Peaks'],
                                   shared_xaxes=False, shared_yaxes=False),
              id='subplots'
              )
])

# Callback function to update the subplots


@app.callback(
    Output('subplots', 'figure'),
    Input('subplots', 'figure')
)
# method to update the subplots
def update_subplots(figure):
    fig = make_subplots(rows=3, cols=3, subplot_titles=['Blue Channel Peaks',
                                                        'Green Channel Peaks',
                                                        'Red Channel Peaks',
                                                        'Hue Channel Peaks',
                                                        'Saturation Channel Peaks',
                                                        'Value Channel Peaks',
                                                        'Luminance Channel Peaks',
                                                        'Red-Green Channel Peaks',
                                                        'Yellow-Blue Channel Peaks'],
                        shared_xaxes=False, shared_yaxes=False)

    # add scatter plots to each subplot
    '''

    * plt.scatter returns a Figure object, which represents the entire figure layout.
    * the .data attribute of the Figure object contains a list of trace objects,
        where each trace represents a data series ot plot.
    * Interested in adding a scatter plot to the subplot.
    * By accessing .data[0], we extract the first (and only) trace object from the list of traces
        returned by px.scatter.
    *We then pass this trace object to fig.add_trace to add it to the subplot at the specified position.
    
    '''

    fig.add_trace(px.scatter(avg_df, x='Conc', y='Peaks_B_avg').data[0], row=1, col=1)
    fig.add_trace(px.scatter(avg_df, x='Conc', y='Peaks_G_avg').data[0], row=1, col=2)
    fig.add_trace(px.scatter(avg_df, x='Conc', y='Peaks_R_avg').data[0], row=1, col=3)
    fig.add_trace(px.scatter(avg_df, x='Conc', y='Peaks_H_avg').data[0], row=2, col=1)
    fig.add_trace(px.scatter(avg_df, x='Conc', y='Peaks_S_avg').data[0], row=2, col=2)
    fig.add_trace(px.scatter(avg_df, x='Conc', y='Peaks_V_avg').data[0], row=2, col=3)
    fig.add_trace(px.scatter(avg_df, x='Conc', y='Peaks_L_avg').data[0], row=3, col=1)
    fig.add_trace(px.scatter(avg_df, x='Conc', y='Peaks_a_avg').data[0], row=3, col=2)
    fig.add_trace(px.scatter(avg_df, x='Conc', y='Peaks_b_avg').data[0], row=3, col=3)

    fig.update_layout(height=1200, showlegend=False)

    return fig


print('TRAP')
# to run the app
if __name__ == '__main__':
    app.run(debug=False)