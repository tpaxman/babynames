library(tidyverse)
#raw_name_choices <- 'Aaron Alex Alexander Archie Cameron Christopher Colin Declan Edward Edwin Ernest Isaac Jude Landen Lane Lawrence Leo Lewis Maxwell Miles Mitchell Nicholas Orson Oscar Patrick Quinn Samuel Sawyer Seth Simon Theodore Thomas Timothy Tyler'
raw_name_choices <- 'Ezra Spencer Ewan Ethan Noah Oliver Liam Aaron Alex Alexander Archie Cameron Ian Colin Declan Edward Isaac Lawrence Leo Lewis Miles Nicholas Quinn Samuel Sawyer Seth Thomas Timothy'
name_choices <- raw_name_choices %>% 
  str_split(' ')

read_csv("alberta-babynames.csv") %>% 
  mutate(name = str_trim(name)) %>% 
  filter(gender == 'Boy') %>% 
  filter(name %in% name_choices[[1]]) %>% 
  ggplot() +
  geom_line(aes(x=year, y=frequency), size=.9) +
  facet_wrap(vars(name), ncol=7) +
  theme_bw() +
  scale_y_continuous(limits = c(0, 500), breaks=c(0,100,200,300,400,500)) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1),
        panel.grid.major.y = element_line(colour = "black", size = 0.05),
        panel.grid.minor.y = element_blank(),
        panel.grid.major.x = element_blank(),
        panel.grid.minor.x = element_blank()
  )
