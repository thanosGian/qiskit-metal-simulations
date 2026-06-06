
from qiskit_metal.qlibrary.qubits.transmon_pocket_cl import TransmonPocketCL

from qiskit_metal.qlibrary.tlines.anchored_path import RouteAnchors

from qiskit_metal.qlibrary.tlines.meandered import RouteMeander

from qiskit_metal.qlibrary.terminations.launchpad_wb_coupled import LaunchpadWirebondCoupled

from qiskit_metal.qlibrary.terminations.launchpad_wb import LaunchpadWirebond

from qiskit_metal import designs, MetalGUI

design = designs.DesignPlanar()

gui = MetalGUI(design)



            # WARNING
#options_connection_pads failed to have a value
Q1 = TransmonPocketCL(
design,
name='Q1',
options={'cl_off_center': '-50um',
 'cl_pocket_edge': '180',
 'connection_pads': {'bus_12': {'cpw_extend': '50um',
                                'cpw_gap': 'cpw_gap',
                                'cpw_width': 'cpw_width',
                                'loc_H': -1,
                                'loc_W': -1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '5um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '125um',
                                'pocket_extent': '5um',
                                'pocket_rise': '65um'},
                     'bus_14': {'cpw_extend': '50um',
                                'cpw_gap': 'cpw_gap',
                                'cpw_width': 'cpw_width',
                                'loc_H': 1,
                                'loc_W': -1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '5um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '110um',
                                'pocket_extent': '5um',
                                'pocket_rise': '65um'},
                     'readout': {'cpw_extend': '50um',
                                 'cpw_gap': 'cpw_gap',
                                 'cpw_width': 'cpw_width',
                                 'loc_H': -1,
                                 'loc_W': 1,
                                 'pad_cpw_extent': '25um',
                                 'pad_cpw_shift': '5um',
                                 'pad_gap': '15um',
                                 'pad_height': '30um',
                                 'pad_width': '70um',
                                 'pocket_extent': '5um',
                                 'pocket_rise': '65um'}},
 'gds_cell_name': 'FakeJunction_01',
 'orientation': '180',
 'pos_x': '-2420um',
 'pos_y': '69um'}
)





            # WARNING
#options_connection_pads failed to have a value
Q2 = TransmonPocketCL(
design,
name='Q2',
options={'cl_off_center': '-50um',
 'cl_pocket_edge': '180',
 'connection_pads': {'bus_12': {'cpw_extend': '50um',
                                'cpw_gap': 'cpw_gap',
                                'cpw_width': 'cpw_width',
                                'loc_H': 1,
                                'loc_W': -1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '5um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '110um',
                                'pocket_extent': '5um',
                                'pocket_rise': '65um'},
                     'bus_23': {'cpw_extend': '50um',
                                'cpw_gap': 'cpw_gap',
                                'cpw_width': 'cpw_width',
                                'loc_H': -1,
                                'loc_W': -1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '5um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '125um',
                                'pocket_extent': '5um',
                                'pocket_rise': '65um'},
                     'readout': {'cpw_extend': '50um',
                                 'cpw_gap': 'cpw_gap',
                                 'cpw_width': 'cpw_width',
                                 'loc_H': -1,
                                 'loc_W': 1,
                                 'pad_cpw_extent': '25um',
                                 'pad_cpw_shift': '5um',
                                 'pad_gap': '15um',
                                 'pad_height': '30um',
                                 'pad_width': '70um',
                                 'pocket_extent': '5um',
                                 'pocket_rise': '65um'}},
 'gds_cell_name': 'FakeJunction_01',
 'orientation': '90',
 'pos_x': '0um',
 'pos_y': '+857.6um'}
)





            # WARNING
#options_connection_pads failed to have a value
Q3 = TransmonPocketCL(
design,
name='Q3',
options={'cl_off_center': '-50um',
 'cl_pocket_edge': '180',
 'connection_pads': {'bus_23': {'cpw_extend': '50um',
                                'cpw_gap': 'cpw_gap',
                                'cpw_width': 'cpw_width',
                                'loc_H': 1,
                                'loc_W': -1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '5um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '110um',
                                'pocket_extent': '5um',
                                'pocket_rise': '65um'},
                     'bus_34': {'cpw_extend': '50um',
                                'cpw_gap': 'cpw_gap',
                                'cpw_width': 'cpw_width',
                                'loc_H': -1,
                                'loc_W': -1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '5um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '125um',
                                'pocket_extent': '5um',
                                'pocket_rise': '65um'},
                     'readout': {'cpw_extend': '50um',
                                 'cpw_gap': 'cpw_gap',
                                 'cpw_width': 'cpw_width',
                                 'loc_H': -1,
                                 'loc_W': 1,
                                 'pad_cpw_extent': '25um',
                                 'pad_cpw_shift': '5um',
                                 'pad_gap': '15um',
                                 'pad_height': '30um',
                                 'pad_width': '70um',
                                 'pocket_extent': '5um',
                                 'pocket_rise': '65um'}},
 'gds_cell_name': 'FakeJunction_01',
 'pos_x': '+2420um',
 'pos_y': '69um'}
)





            # WARNING
#options_connection_pads failed to have a value
Q4 = TransmonPocketCL(
design,
name='Q4',
options={'cl_off_center': '-50um',
 'cl_pocket_edge': '180',
 'connection_pads': {'bus_14': {'cpw_extend': '50um',
                                'cpw_gap': 'cpw_gap',
                                'cpw_width': 'cpw_width',
                                'loc_H': -1,
                                'loc_W': -1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '5um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '125um',
                                'pocket_extent': '5um',
                                'pocket_rise': '65um'},
                     'bus_34': {'cpw_extend': '50um',
                                'cpw_gap': 'cpw_gap',
                                'cpw_width': 'cpw_width',
                                'loc_H': 1,
                                'loc_W': -1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '5um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '110um',
                                'pocket_extent': '5um',
                                'pocket_rise': '65um'},
                     'readout': {'cpw_extend': '50um',
                                 'cpw_gap': 'cpw_gap',
                                 'cpw_width': 'cpw_width',
                                 'loc_H': -1,
                                 'loc_W': 1,
                                 'pad_cpw_extent': '25um',
                                 'pad_cpw_shift': '5um',
                                 'pad_gap': '15um',
                                 'pad_height': '30um',
                                 'pad_width': '70um',
                                 'pocket_extent': '5um',
                                 'pocket_rise': '65um'}},
 'gds_cell_name': 'FakeJunction_01',
 'orientation': '270',
 'pos_x': '0um',
 'pos_y': '-857.6um'}
)




cpw1 = RouteMeander(
design,
name='cpw1',
options={'_actual_length': '9.899999999999997 '
                   'mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '250um',
          'start_jogged_extension': '',
          'start_straight': '100um'},
 'meander': {'asymmetry': '-413.75um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Q4',
                            'pin': 'bus_14'},
                'start_pin': {'component': 'Q1',
                              'pin': 'bus_14'}},
 'total_length': '9.9mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




cpw2 = RouteMeander(
design,
name='cpw2',
options={'_actual_length': '9.299999999999999 '
                   'mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '250um',
          'start_jogged_extension': '',
          'start_straight': '100um'},
 'meander': {'asymmetry': '+413.75um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Q4',
                            'pin': 'bus_34'},
                'start_pin': {'component': 'Q3',
                              'pin': 'bus_34'}},
 'total_length': '9.3mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




cpw3 = RouteMeander(
design,
name='cpw3',
options={'_actual_length': '9.6 mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '250um',
          'start_jogged_extension': '',
          'start_straight': '100um'},
 'meander': {'asymmetry': '-551.75um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Q2',
                            'pin': 'bus_23'},
                'start_pin': {'component': 'Q3',
                              'pin': 'bus_23'}},
 'total_length': '9.6mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




cpw4 = RouteMeander(
design,
name='cpw4',
options={'_actual_length': '10.300000000000002 '
                   'mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '250um',
          'start_jogged_extension': '',
          'start_straight': '100um'},
 'meander': {'asymmetry': '+551.75um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Q2',
                            'pin': 'bus_12'},
                'start_pin': {'component': 'Q1',
                              'pin': 'bus_12'}},
 'total_length': '10.3mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Launch_CL_Q1 = LaunchpadWirebond(
design,
name='Launch_CL_Q1',
options={'lead_length': '0um',
 'orientation': '90',
 'pos_x': '-3545um',
 'pos_y': '-2812um'},

component_template=None,
)




Launch_CL_Q2 = LaunchpadWirebond(
design,
name='Launch_CL_Q2',
options={'lead_length': '0um',
 'orientation': '270',
 'pos_x': '-3545um',
 'pos_y': '2812um'},

component_template=None,
)




Launch_CL_Q3 = LaunchpadWirebond(
design,
name='Launch_CL_Q3',
options={'lead_length': '0um',
 'orientation': '270',
 'pos_x': '3545um',
 'pos_y': '2812um'},

component_template=None,
)




Launch_CL_Q4 = LaunchpadWirebond(
design,
name='Launch_CL_Q4',
options={'lead_length': '0um',
 'orientation': '90',
 'pos_x': '3545um',
 'pos_y': '-2812um'},

component_template=None,
)




Launch_RO_Q1 = LaunchpadWirebondCoupled(
design,
name='Launch_RO_Q1',
options={'lead_length': '30um',
 'orientation': '0',
 'pos_x': '-4020um',
 'pos_y': '0'},

component_template=None,
)




Launch_RO_Q2 = LaunchpadWirebondCoupled(
design,
name='Launch_RO_Q2',
options={'lead_length': '30um',
 'orientation': '270',
 'pos_x': '990um',
 'pos_y': '2812um'},

component_template=None,
)




Launch_RO_Q3 = LaunchpadWirebondCoupled(
design,
name='Launch_RO_Q3',
options={'lead_length': '30um',
 'orientation': '180',
 'pos_x': '4020um',
 'pos_y': '0'},

component_template=None,
)




Launch_RO_Q4 = LaunchpadWirebondCoupled(
design,
name='Launch_RO_Q4',
options={'lead_length': '30um',
 'orientation': '90',
 'pos_x': '-990um',
 'pos_y': '-2812um'},

component_template=None,
)




Readout1 = RouteMeander(
design,
name='Readout1',
options={'_actual_length': '8.7 mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '0um',
          'start_jogged_extension': '',
          'start_straight': '430um'},
 'meander': {'asymmetry': '+150um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Launch_RO_Q1',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q1',
                              'pin': 'readout'}},
 'total_length': '8.7 mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Readout3 = RouteMeander(
design,
name='Readout3',
options={'_actual_length': '8.3 mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '0um',
          'start_jogged_extension': '',
          'start_straight': '430um'},
 'meander': {'asymmetry': '+150um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Launch_RO_Q3',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q3',
                              'pin': 'readout'}},
 'total_length': '8.3 mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Readout2 = RouteMeander(
design,
name='Readout2',
options={'_actual_length': '8.500000000000002 '
                   'mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '0um',
          'start_jogged_extension': '',
          'start_straight': '535um'},
 'meander': {'asymmetry': '+200um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Launch_RO_Q2',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q2',
                              'pin': 'readout'}},
 'total_length': '8.5 mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Readout4 = RouteMeander(
design,
name='Readout4',
options={'_actual_length': '8.0 mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '0um',
          'start_jogged_extension': '',
          'start_straight': '535um'},
 'meander': {'asymmetry': '+200um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Launch_RO_Q4',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q4',
                              'pin': 'readout'}},
 'total_length': '8.0 mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Charge_Line1 = RouteAnchors(
design,
name='Charge_Line1',
options={'_actual_length': '3.4152517741486648 '
                   'mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '225um',
          'start_jogged_extension': OrderedDict([(0,
                                                  ['L',
                                                   '200um'])]),
          'start_straight': '120um'},
 'pin_inputs': {'end_pin': {'component': 'Launch_CL_Q1',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q1',
                              'pin': 'Charge_Line'}},
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Charge_Line3 = RouteAnchors(
design,
name='Charge_Line3',
options={'_actual_length': '3.277251774148665 '
                   'mm',
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '225um',
          'start_jogged_extension': OrderedDict([(0,
                                                  ['L',
                                                   '200um'])]),
          'start_straight': '120um'},
 'pin_inputs': {'end_pin': {'component': 'Launch_CL_Q3',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q3',
                              'pin': 'Charge_Line'}},
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Charge_Line2 = RouteAnchors(
design,
name='Charge_Line2',
options={'_actual_length': '4.865735698864887 '
                   'mm',
 'anchors': {0: array([-2. ,  2.5])},
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '100um',
          'start_jogged_extension': OrderedDict([(0,
                                                  ['L',
                                                   '300um'])]),
          'start_straight': '400um'},
 'pin_inputs': {'end_pin': {'component': 'Launch_CL_Q2',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q2',
                              'pin': 'Charge_Line'}},
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Charge_Line4 = RouteAnchors(
design,
name='Charge_Line4',
options={'_actual_length': '4.865735698864887 '
                   'mm',
 'anchors': {0: array([ 2. , -2.5])},
 'fillet': '99.99um',
 'lead': {'end_jogged_extension': '',
          'end_straight': '225um',
          'start_jogged_extension': OrderedDict([(0,
                                                  ['L',
                                                   '300um'])]),
          'start_straight': '400um'},
 'pin_inputs': {'end_pin': {'component': 'Launch_CL_Q4',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q4',
                              'pin': 'Charge_Line'}},
 'trace_gap': 'cpw_gap'},

type='CPW',
)



gui.rebuild()
gui.autoscale()
        