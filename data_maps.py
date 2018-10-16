
""" 
The groupings below map specific data-based claimed types to larger 
groupings. For example: nIa, Ia, Ia*, and Ia-HV all map to Ia.
Any new claimed types to be considered in the analysis need to be added 
here and mapped to a larger group, which also needs to be in cat_code
"""
groupings = {
#     Ia
    'nIa' : 'Ia',
    'Ia' : 'Ia',
    'Ia*' :'Ia',
    'Ia-HV' :'Ia',
#     'Ia-91T'
    'Ia-91T' : 'Ia-91T',
#     'Ia-91bg'
    'Ia-91bg' : 'Ia-91bg',
#     'Ib/Ic'
    'IIb/Ib/Ic (Ca rich)' : 'Ib/Ic',
    'Ib/Ic (Ca rich)' : 'Ib/Ic',
    'Ib (Ca rich)' : 'Ib/Ic',
#     'Ia CSM'
    'Ia CSM' : 'Ia CSM',
#     'Ia-02cx'
    'Ia-02cx' : 'Ia-02cx',
    'Iax[02cx-like]' : 'Ia-02cx',
#     'II P'
    'II P' : 'II P',
    'II-p' : 'II P',
    'II Pec' : 'II P',
    'II P Pec' : 'II P',
#     'II?' : 'II P',
#     'II Pec?' : 'II P',
#     'IIP?' : 'II P',
    'II' : 'II P',
#     'IIn'
    'IIn' : 'IIn',
    'IIn Pec' : 'IIn',
    'LBV to IIn' : 'IIn',
    'IIn-pec/LBV' : 'IIn',
#     'IIn?' : 'IIn',
#     'Ib'
    'Ib' : 'Ib',
    'Ibn' : 'Ib',
#     'Ic'
    'Ic' : 'Ic',
#     'Ic?' : 'Ic',
    'Ic-lum?' : 'Ic',
    'Ic Pec' : 'Ic',
#     Ic BL
    'Ic BL' : 'Ic BL',
    'BL-Ic' : 'Ic BL',
#     'SLSN-II?'
#     'SLSN-II?' : 'SLSN-II?',
#     'SLSN-I'
    'SLSN-I' : 'SLSN-I',
#     'LGRB'
    'LGRB' : 'LGRB'
}


"""
Claimed Type categories, mapped to integer values.
The integer values are used by the ML model.
""" 
cat_code = {
    'Other' : 0,
    'LGRB': 1,
    'Ia' : 2, 
    'II P': 3, 
    'Ib' : 4,
    'Ic' : 5, 
    'IIn': 6, 
    'SLSN-I' : 7, 
    'Ia-02cx' : 8,
    'Ic BL' : 9, 
    'SLSN-II?': 10, 
    'Ia-91bg' : 11, 
    'Ia-91T' : 12, 
    'Ia CSM' : 13
    
}



# col_lists = {
# 'ned_mass_cols': ['NED_2MASS_J', 'NED_2MASS_H', 'NED_2MASS_Ks'],

# # ned_sdss_cols = ['NED_SDSS_u', 'NED_SDSS_g', 'NED_SDSS_r', 'NED_SDSS_i', 'NED_SDSS_z']

# # ned_galex_cols = ['NED_GALEX_NUV', 'NED_GALEX_FUV']

# # ned_iras_cols = ['NED_IRAS_12m', 'NED_IRAS_25m', 'NED_IRAS_60m', 'NED_IRAS_100m', 'NED_HI_21cm', 'NED_1p4GHz']

# # all_ned_cols = [col for col in list(data_df) if "NED_" in col] # All NED_

# # hyperleda = [col for col in list(data_df) if "HyperLEDA" in col] 

# 'allwise' : [col for col in list(data_df) if "AllWISE" in col and "Err" not in col],

# 'firefly_cols' : [col for col in list(data_df) if "Firefly" in col], # Firefly

# 'mpa_cols' : [col for col in list(data_df) if "MPAJHU" in col], # MPAJHU

# 'zoo_cols' : [col for col in list(data_df) if "Zoo" in col], # GalaxyZoo

# 'gswlc' : [col for col in list(data_df) if "GSWLC" in col], # GSWLC

# 'wiscpca' : [col for col in list(data_df) if "WiscPCA" in col], # WiscPCA

# 'nsa' : [col for col in list(data_df) if "NSA_" in col], # NSA

# 'nsa_k' : [col for col in list(data_df) if "NSA_" in col and "KCORRECT_" in col], # NSA

# 'scos' : [col for col in list(data_df) if "SCOS_" in col], # SCOS

# 'ps1' : [col for col in list(data_df) if "PS1" in col] # PS1

# # 'full' : scos + ps1 + nsa + wiscpca + gswlc + zoo_cols + mpa_cols
# }