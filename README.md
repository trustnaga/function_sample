# Function Sample

This Sample is Durable Function 
To Deploy to Azure Function 

-  Install the dependencies
<pre>
pip install -r requirements.txt  --target ./.python_packages/lib/site-packages
</pre>

- Deploy using Azure Function Tools

<pre>
func azure functionapp publish funtionName --no-build --force
</pre>