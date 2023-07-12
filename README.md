# HadCM3 data viewer

This is a work in progress. The HadCM3 (Hadley Center Coupled Model v3) is a General Circulation Model - a climatic model - whose data was published in the Third Assessment Report (TAR) by the IPCC (Intergovernmental Panel for Climate Change). The data consists of climate change projections considering different scenarios of GHG emissions, defined by the IPCC. You can find the original files and more information about the panel and the model here: https://www.ipcc-data.org/sim/gcm_clim/SRES_TAR/hadcm3_download.html and also here https://www.metoffice.gov.uk/research/approach/modelling-systems/unified-model/climate-models/hadcm3.

You can find the same files converted to a more useful CSV, which also accounts for the latitude and longitude of the grid cell centers, to identify the climate data geographically; which also helps for the visualization. Bear in mind that the majority of the information illustrates the difference between the projected climate to a reference period.

According to WMO (World Meteorological Organization), "for historical comparison and climate change monitoring, WMO still recommends the continuation of the 1961-1990 period for the computation and tracking global climate anomalies relative to a fixed and common reference period.", so, the HadCM3 is, still, a trusted source of data for climate studies.

Also, in the future, I intend to expand this tool to generate climate files to be used in various simulations. There is already a tool capable of adapting climate files to consider climate change, which is called CCWorldWeatherGen, developed by the University of South Hampton. The tool is a spreadsheet tool where the user needs to download the correct HadCM3 data and add it to the specific directory in order to use this tool. Aside from citing the impracticality of doing this, it is impossible not to mention the slow speed of the process, and the numerous errors that come with it. The "third" step would be the development of an EnergyPlus Python plug-in that generates the data for the next 10 to 20 years (probably using some time series techniques or even NN) to predict the building's behavior in climate change scenarios.

I'm mainly using notebooks for the development phase; also because I've been trying some interactive libraries and the best ones (or the ones that worked) are for jupyter notebooks. Don't mind the commits in such an early stage, I'm also practicing git/versioning. Please, if you have any suggestions or questions, don't hesitate to contact me.
