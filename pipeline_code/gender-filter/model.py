#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:07:21 2019

@author: winstonlin
"""
import torch 
import torch.nn as nn


class LSTMnet(torch.nn.Module): 
    def __init__(self, input_dim, hidden_dim, output_dim, num_layers):
        super(LSTMnet, self).__init__()
        # Net Parameters
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.num_layers = num_layers
        
        # LSTM-layers
        self.lstm = nn.Sequential()
        self.lstm.add_module( "lstm", nn.LSTM(self.input_dim, self.hidden_dim, self.num_layers, dropout=0.5, batch_first=True, bidirectional=False) )
       
        # Dense-layers
        self.dense = nn.Sequential()
        self.dense.add_module( "dense1", nn.Linear(self.hidden_dim, 100) )
        self.dense.add_module( "relu1", nn.LeakyReLU() )
        self.dense.add_module( "dense2", nn.Linear(100, 50) )
        self.dense.add_module( "relu2", nn.LeakyReLU() )
        self.dense.add_module( "dense_out", nn.Linear(50, self.output_dim) )
        self.dense.add_module( "act_out", nn.Sigmoid() ) 
        
    def forward(self, inputs):
        blstm_out, (hidden,cell) = self.lstm(inputs)       
        dense_out = self.dense(blstm_out[:,-1,:])       # Only take the last-time output
        return dense_out        

