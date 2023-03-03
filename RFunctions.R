skew_list = function(df){
  skew_list = c()
  
  for (field in colnames(df)){
    print(field)
    vec = df[[field]]
    skw = skewness(vec)
    print(skw)
    
    if((skw < -0.5) | (skw > 0.5)){
      paste(field, "this is skewed and requires transformation.")
      skew_list = append(skew_list, field)
    }
    
  }
  return(skew_list)
}