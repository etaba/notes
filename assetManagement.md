#Yarn
A javascript package manager that acts like a wrapper of sorts for npm.
Install with `npm install yarn`
Initialize the yarn project, which will create a `package.json` configuration file and `node_modules` folder which will hold the actual libraries
`yarn init`
`package.json` should be added to the repository while `node_modules` should be ignored 
Add the relevant javascript libraries like so
`yarn add boostrap`
Now in other systems all the dependencies can be installed using the packages.json file with the command `yarn install`