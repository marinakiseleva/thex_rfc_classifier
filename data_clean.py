

from data_maps import groupings

def group_cts(valid_df):
    # Group claimed types into supergroups, defined in groupings dict
    valid_df['claimedtype_group'] = valid_df.apply(lambda row:  
                                             groupings[row.claimedtype] 
                                             if row.claimedtype in groupings 
                                             else None,
                                             axis=1)

    # Dataframe of claimed types that do not have group
    ungrouped_types = list(set(valid_df.claimedtype.unique()) - set(groupings.keys()))
    print(str(len(ungrouped_types)) + " rows with ungrouped claimed type.")

    # Claimed Types that need to be grouped
    add_cts = []
    for ct in list(valid_df.claimedtype.unique()):
        if "," not in ct and ct != '' and ct not in groupings:
            add_cts.append(ct)
    # Drop rows with no grouped claimed type      
    valid_df = valid_df[~valid_df['claimedtype_group'].isnull()]
    print ("Remaining rows in valid dataframe: " + str(valid_df.shape[0]))
    
    return valid_df




