
%{ 

everything in here is a comment 

%}

% path is the folders currently in Matlab 

% how can we set our path? 

%can use the gui and click set path

%can use this command 
addpath(genpath('~/Documents/'))

% when creating a vector you use commas or spaces to separate values.
% Semicolons separate rows 

%how do we index?

%use round brackets 

% 1 index language not a 0 index language

% use colon to index the whole row

% can transpose with an '

% to add a new number you index the location and then add equals 

% how do you get rid of a column?

%you use empty square brackets 

% save by creating the file names and the variables 
% then you can load it using load .mat

% why do we have to be careful about division and multiplication in matlab 
% does matrix multiplication and division 

% item wise multiplication and division use a period 

% can use the help function to learn more about things 

%logical operations 
%double == is equal to 
% don't use and or or use & | respectively 

1==0

% if i want to supress printing to the terminal use a semicolon at the end 

%syntax of if statements are different. Do not care about indentations.
%Finish it off with an end 

%in matlab it is elseif not elif 

%conditionals 

%switch case?

% we have for and while loops 
% need to include end at the end of the loops

%tic toc evaluates the amount of time between tic and toc 

%while loop keeps going until a condition is false 

% can use smart indent to properly indent it 

% continue breaks out of a block of code while remaining in the loop 
%break will exit completely out of a loop

%parfor. which allows you to run loops in parallel 

% setsize == 4 returns a mask with boolean values. 

% there are functions in matlab. Can be part of a larger script or a
% standalone script 

% function is called subtractone in the brackets is the argument we are
% passing it 
% in python if we wanted to a return an array we use return. Instead you
% have to have it at the beginning of the function 

%variables can be either local or global. 

% nargin - number of arguments inputted 

% can add help files to your functions 

% try catch 
% will try some commands and if they fail then catch and move onto the next
% set of other commands 

%my text with single quotes becomes an array, my text with double quotes
%creates a string 

%sprintf - string print format. 

% %s interprets this as a string 

%fprintf - write text to a file 

% open a file using fopen 
% w stands for writing privilege

%cells are similar to Pandas DF

cell1 = {'apples', 'oranges'}

cell1{1}

cell2 = {[1,2,3,4,5], [1,2,3,4,5,6]} % numbers in each are not equal

cell2{1}(5) % take the first cell and index the 5th element 

cell2{3}= "does this work" % can mix types 

% structures are like cells, but are named variables within each element 

data.subject = "sme"

data(:).subject

data.subject(1).block(2).trial(50).RT = .765

