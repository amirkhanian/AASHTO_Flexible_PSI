"""
    TYPE_3_AASHTO_RT_Flex_PSI.py

    A Type 3 nomograph that represents the original PSI equation for flexible
    pavements as developed in the AASHO Road Test.
    
    The equation is described in detail: Highway Research Board Special 
    Report 61E (1962) on pages 14 and 23:
        
        p = 5.03 - 1.91 * log(1 + SV) - 0.01 * sqrt(C+P) - 1.38 * RD^2
        
        where:
            
            p = present serviceability index, unitless
            SV = slope vairance mean, degrees
            C+P = cracking and patching, with C as cracked area per 1000 ft^2
                        and P as the patched area per 1000 ft^2
            RD = rutting, inches
            
    The mathematical work to generate the nomograph was performed by
    
    Armen Amirkhanian
    
    The resulting code/software is a modification of an example file
    in the pynomo package. This modified code is released under the terms
    of the GNU General Public License, either version 3 or a later version
    at the user's discretion. The original copyright and license notice for
    the example file is below.

    Copyright (C) 2007-2009  Leif Roschier

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    This process would have been impossible without the incredible pynomo
    package from Leif Roschier!
"""
import sys
import numpy as np

sys.path.insert(0, "..")
from pynomo.nomographer import Nomographer

p_params = {
    'u_min': 0.0,
    'u_max': 5.0,
    'function': lambda u: -u,
    'title': r'$p$ (Present Serviceability Index)',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'scale_type': 'linear smart'
}

SV_params = {
    'u_min': 0.1,
    'u_max': 10.0,
    'function': lambda u: 5.03-1.91*np.log10(1+u),
    'title': r'$SV$ (Slope Variance, deg)',
    'tick_levels': 2,
    'tick_text_levels': 1,
    'scale_type': 'log smart',
}

CP_params = {
    'u_min': 10.0,
    'u_max': 2000.0,
    'function': lambda u: -0.01*np.sqrt(u),
    'title': r'$C+P$ (Cracking and Patching, ft$^2$/2000 ft$^2$)',
    'tick_levels': 2,
    'tick_text_levels': 1,
    'scale_type': 'log smart',
}

RD_params = {
    'u_min': 0.1,
    'u_max': 1.5,
    'function': lambda u: -1.38*u**2,
    'title': r'$RD$ (Rutting Depth, in)',
    'tick_levels': 2,
    'tick_text_levels': 1,
    'scale_type': 'linear smart',
}

block_1_params = {
    'block_type': 'type_3',
    'width': 10.0,
    'height': 10.0,
    'f_params': [RD_params,SV_params,p_params,CP_params],
    'reference_titles':['Turning Line'],
    'isopleth_values': [[1, 2, 'x', 200]],
}

main_params = {
    'filename': 'TYPE_3_AASHTO_RT_Flex_PSI.pdf',
    'paper_height': 20.0,
    'paper_width': 20.0,
    'block_params': [block_1_params],
    'transformations': [('rotate', 0.01), ('scale paper',)],
    'title_str': r'$p=5.03-1.91\log(1+SV)-0.01\sqrt{C+P}-1.38RD^2$',
    'title_y': 21.0,
}
Nomographer(main_params)
