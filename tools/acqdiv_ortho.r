## DONT DO THAT BOTH HAVE SAME NAMES IE WRITTEN OVER THE OTHER ##
library(dplyr)

get_right_sessions <- function(sp,a=4){ #sp: speakers dataset, a: limit max age#
  underage <- sp[,c("session_id_fk", "age", "role_raw","speaker_label")]
  underage <- underage[as.character(underage$role_raw)=="Target_Child",]
  
  underage <- underage %>% filter(as.character(age)<a)
  selected <- utterances %>% filter(session_id_fk %in% underage$session_id_fk, !(speaker_label %in% underage$speaker_label))
  return(selected)
}

## RUSSIAN ## and maybe others
load("/Users/gladysbaudet/Desktop/PFE/acqdiv_corpus_2017-09-28_CRJ.rda")

rus_speakers <- speakers[speakers$language=="Russian",]

write.table(get_right_sessions(rus_speakers)$utterance, sep="\n", file="/Users/gladysbaudet/Desktop/PFE/CDS/russian/ortholines.txt", 
            row.names=FALSE, col.names=FALSE, quote=FALSE, na="")

## TURKISH ##
load("/Users/gladysbaudet/Desktop/PFE/CDS/turkish/acqdiv_corpus_2017-09-28_turkish.rData")

tur_speakers <- speakers[speakers$language=="Turkish",]

write.table(get_right_sessions(tur_speakers)$utterance, sep="\n", file="/Users/gladysbaudet/Desktop/PFE/CDS/turkish/ortholines.txt", 
            row.names=FALSE, col.names=FALSE, quote=FALSE, na="")
