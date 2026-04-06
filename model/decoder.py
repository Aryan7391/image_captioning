# model/decoder.py — LSTM Decoder

import torch
import torch.nn as nn

class DecoderLSTM(nn.Module):
    def __init__(self, embed_size, hidden_size, vocab_size, num_layers=1):
        super(DecoderLSTM, self).__init__()

        # Word embedding layer
        # Converts word index → dense vector
        self.embed = nn.Embedding(vocab_size, embed_size)

        # LSTM layer
        # Takes word embedding + image features → predicts next word
        self.lstm = nn.LSTM(
            input_size=embed_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True
        )

        # Final linear layer
        # Maps LSTM output → vocabulary scores
        self.linear = nn.Linear(hidden_size, vocab_size)

        # Dropout to prevent overfitting
        self.dropout = nn.Dropout(0.3)

    def forward(self, features, captions):
        # Embed the caption words
        embeddings = self.dropout(self.embed(captions))      # (batch, seq_len, embed_size)

        # Concatenate image features + word embeddings
        # Image features act as the first "word"
        features = features.unsqueeze(1)                     # (batch, 1, embed_size)
        inputs = torch.cat((features, embeddings), dim=1)   # (batch, seq_len+1, embed_size)

        # Pass through LSTM
        lstm_out, _ = self.lstm(inputs)                      # (batch, seq_len+1, hidden_size)

        # Get vocabulary scores
        outputs = self.linear(lstm_out)                      # (batch, seq_len+1, vocab_size)
        return outputs

    def generate_caption(self, features, vocab, max_length=20):
        caption = []

        # Initialize LSTM state with image features
        inputs = features.unsqueeze(1)                       # (1, 1, embed_size)
        states = None

        for _ in range(max_length):
            # One step through LSTM
            lstm_out, states = self.lstm(inputs, states)     # (1, 1, hidden_size)

            # Get word scores
            outputs = self.linear(lstm_out.squeeze(1))       # (1, vocab_size)

            # Pick word with highest score
            predicted = outputs.argmax(1)                    # (1,)

            # Get the word string
            word = vocab.idx2word[predicted.item()]

            # Stop if <end> token
            if word == '<end>':
                break

            # Skip special tokens
            if word not in ['<start>', '<pad>', '<unk>']:
                caption.append(word)

            # Next input is the predicted word embedding
            inputs = self.embed(predicted).unsqueeze(1)      # (1, 1, embed_size)

        return ' '.join(caption)