

from data_maps import groupings

def group_cts(valid_df):
    """
    Normalizes claimed type (transient type) into a specific category (one of the values in the groupings map). If claimed type is not in map, it is given a new claimed type value of NULL.
    :param valid_df: Pandas DataFrame of galaxy/transient data. Must have column 'claimedtype' with transient type
    :return valid_df: Returns Pandas DataFrame with new column claimedtype_group, which has normalized transient type for each galaxy. 
    """
    new_column = 'claimedtype_group'
    # Group claimed types into supergroups, defined in groupings dict
    valid_df[new_column] = valid_df.apply(lambda row:  
                                             groupings[row.claimedtype] 
                                             if row.claimedtype in groupings 
                                             else None,
                                             axis=1)

    # Dataframe of claimed types that do not have group
    ungrouped_types = list(set(valid_df.claimedtype.unique()) - set(groupings.keys()))

    
    # Drop rows with no grouped claimed type      
    valid_df = valid_df[~valid_df[new_column].isnull()]
    
    return valid_df




