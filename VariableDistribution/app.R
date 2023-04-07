#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(plotly)
library(ggplot2)
library(readr)
mp = read_csv("https://github.com/Derek-Kirk/Rocket_League/blob/cd8b6dbbf3577b8280e1d32b914d24f25a799784/matches_by_players.csv?raw=true")
data = mp[,8:dim(mp)[2]-2] # Dropping ids, players, winner indicator, and team score.
cols = colnames(data)
# joined_data = read_csv("https://github.com/Derek-Kirk/Rocket_League/blob/main/joined_data.csv?raw=true")
# Define UI for application that draws a histogram

ui <- fluidPage(

    # Application title
    titlePanel("Variable Distribution"),

    # Sidebar with a slider input for number of bins 
    sidebarLayout(
        sidebarPanel(
            selectInput("var", "Select a variable.", cols)
        ),

        # Show a plot of the generated distribution
        mainPanel(
           plotlyOutput("varHist")
        )
    )
)

# Define server logic required to draw a histogram
server <- function(input, output) {

    
    output$varHist = renderPlotly({
      ggplot()+
        geom_histogram(aes(x = data[[input$var]], y = after_stat(density)),
                     fill = "purple")+
        geom_density(aes(x = data[[input$var]]),
                     alpha = 0.6)+
        labs(x = input$var, y = "c o u n t")
    })
}

# Run the application 
shinyApp(ui = ui, server = server)
