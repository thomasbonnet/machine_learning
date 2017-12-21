##espace memoire d'un dataframe y compris les colonnes de type object
df_products_prior.info(memory_usage='deep')
## espace memoire colonne par colonne en MBytes
df_products_prior.memory_usage()/1000000.
