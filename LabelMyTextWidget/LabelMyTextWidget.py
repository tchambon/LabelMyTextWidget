import ipywidgets as widgets
from IPython.display import display
from ipywidgets import Button, HBox, VBox
import pandas as pd
import numpy as np


__all__ = ['LabelMyTextWidget']

class LabelMyTextWidget:
    """ 
    Widget to quickly label a dataframe containing a column with text data and a column with target labels.
    
    """
    def __init__(self, df_source, content_column, class_list, class_id, output_column, unclassified_value=-1, randomize=False):
        """
        Create a LabelMyTextWidget object.
 
        :param df_source: The pandas dataframe containing the data column and the label column (to fill by the widget)
        :param content_column: The name of the column containing the text data to label
        :param class_list: List of the label type names (ex: Positive, Negative, Neutral)
        :param class_id: The id of each label type
        :param output_column: Name of the column to complete with labels
        :param unclassified_value: Value of the unclassified rows for the output_column
        :param randomize: If true, the labeling order will be random. If False, it will follow the index numbers

 
        :Example:
        >>> df['text'] = 'example of text content to label'
        >>> df['label'] = -1
        >>> LabelMyText(df, 'text', ['positive', 'negative'], [1, 0], 'label', unclassified_value=-1)
        """
        
        self.df_source = df_source
        self.content_column = content_column
        self.output_column = output_column
        self.unclassified_value = unclassified_value
        self.randomize = randomize
        
        
        self.items = [ButtonLabeling(class_id = class_id[i],description=l) for i, l in enumerate(class_list)]
        self.items.append(ButtonLabeling(class_id = unclassified_value, description='Skip', button_style='warning'))

        for button in self.items:
            button.on_click(self.on_button_clicked_t)



        self.out = widgets.Output(layout={'border': '1px solid black'})
        self.out.append_stderr('Text is coming here')

        button_box = HBox([widgets.Label(value="Label"), *self.items])

        self.box = VBox([button_box, self.out])  
        
        self.df_explore = self.df_source[self.df_source[output_column] == unclassified_value].index
        self.cursor = 0
        
        if randomize:
            self.df_explore = np.random.permutation(self.df_explore)
            
        self.out.clear_output(wait=True)
        
        
    def display(self):
        """
        Display the widget
        """
        display(self.box)
        self.display_next_row()
        
    def on_button_clicked_t(self, b):
        #print(f"TEST Button clicked: {b.description}, {b.class_id}")
        if (self.cursor) <= len(self.df_explore) and len(self.df_explore) > 0: 
            self.df_source.loc[self.df_explore[self.cursor - 1], self.output_column] = {b.class_id}
        self.display_next_row()
        
    def display_next_row(self):
        #pdb.set_trace()
        if (self.cursor) >= len(self.df_explore): 
            with self.out:
                self.out.clear_output()
                print('Finished: All rows have been processed')
            return
        
        next_text = str(self.df_source[self.content_column].loc[self.df_explore[self.cursor]])
        with self.out:
            print(f'Row index: {self.df_explore[self.cursor]} | Number of row processed : {self.cursor} \n')
            print(f'{next_text}')
        
        
        self.cursor += 1
        self.out.clear_output(wait=True)
      
            
        
 

class ButtonLabeling(Button):
    def __init__(self, class_id, *args, **kwargs):
        self.class_id = class_id
        super().__init__(*args, **kwargs)
    