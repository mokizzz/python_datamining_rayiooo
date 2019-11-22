import numpy as np
import torch
import torch.nn.functional as F
from torch import nn
from torch.utils.data import Dataset, DataLoader


class MyNet_v2_1(nn.Module):
    def __init__(self, in_dim, out_dim=2):
        super(MyNet_v2_1, self).__init__()

        in_dim = in_dim+1+1+12+5+6+10
        self.embed_sex = nn.Embedding(3, 2)
        self.embed_access_freq = nn.Embedding(5, 2)
        self.embed_multi_a = nn.Embedding(2561, 13)
        self.embed_multi_b = nn.Embedding(291, 6)
        self.embed_multi_c = nn.Embedding(428, 7)
        self.embed_multi_d = nn.Embedding(1556, 11)
        self.embed_multi_e = nn.Embedding(2, 1)
        self.bn0 = nn.BatchNorm1d(in_dim)
        self.bn1 = nn.BatchNorm1d(2048)
        self.bn2 = nn.BatchNorm1d(1024)
        self.bn3 = nn.BatchNorm1d(512)
        self.bn4 = nn.BatchNorm1d(256)
        self.bn5 = nn.BatchNorm1d(128)
        self.bn6 = nn.BatchNorm1d(64)
        self.bn7 = nn.BatchNorm1d(32)
        self.bn8 = nn.BatchNorm1d(16)
        self.bn9 = nn.BatchNorm1d(8)
        self.fc1 = nn.Linear(in_dim, 2048)
        self.fc2 = nn.Linear(2048, 1024)
        self.fc3 = nn.Linear(1024, 512)
        self.fc4 = nn.Linear(512, 256)
        self.fc5 = nn.Linear(256, 128)
        self.fc6 = nn.Linear(128, 64)
        self.fc7 = nn.Linear(64, 32)
        self.fc8 = nn.Linear(32, 16)
        self.fc9 = nn.Linear(16, 8)
        self.fc10 = nn.Linear(8, out_dim)
        self.relu = nn.ReLU(inplace=True)


    def forward(self, x):
        sex = self.embed_sex(x[:, -7].long())
        access_freq = self.embed_access_freq(x[:, -6].long())
        multi_a = self.embed_multi_a(x[:, -5].long())
        multi_b = self.embed_multi_b(x[:, -4].long())
        multi_c = self.embed_multi_c(x[:, -3].long())
        multi_d = self.embed_multi_d(x[:, -2].long())
        multi_e = self.embed_multi_e(x[:, -1].long())

        out = x[:, :-7]
        out = torch.cat(
            (out, sex, access_freq, multi_a, multi_b, multi_c, multi_d, multi_e), dim=1)
        
        out = self.fc1(self.bn0(out))
        out = self.fc2(self.relu(self.bn1(out)))
        out = self.fc3(self.relu(self.bn2(out)))
        out = self.fc4(self.relu(self.bn3(out)))
        out = self.fc5(self.relu(self.bn4(out)))
        out = self.fc6(self.relu(self.bn5(out)))
        out = self.fc7(self.relu(self.bn6(out)))
        out = self.fc8(self.relu(self.bn7(out)))
        out = self.fc9(self.relu(self.bn8(out)))
        out = self.fc10(self.relu(self.bn9(out)))
        return out
    
    
class MyNet_v2(nn.Module):
    def __init__(self, in_dim, out_dim=2):
        super(MyNet_v2, self).__init__()

        in_dim = in_dim+1+1+12+5+6+10
        self.embed_sex = nn.Embedding(3, 2)
        self.embed_access_freq = nn.Embedding(5, 2)
        self.embed_multi_a = nn.Embedding(2561, 13)
        self.embed_multi_b = nn.Embedding(291, 6)
        self.embed_multi_c = nn.Embedding(428, 7)
        self.embed_multi_d = nn.Embedding(1556, 11)
        self.embed_multi_e = nn.Embedding(2, 1)
        self.bn0 = nn.BatchNorm1d(in_dim)
        self.bn1 = nn.BatchNorm1d(2048)
        self.bn2 = nn.BatchNorm1d(1024)
        self.bn3 = nn.BatchNorm1d(512)
        self.bn4 = nn.BatchNorm1d(256)
        self.bn5 = nn.BatchNorm1d(128)
        self.bn6 = nn.BatchNorm1d(64)
        self.bn7 = nn.BatchNorm1d(32)
        self.bn8 = nn.BatchNorm1d(16)
        self.bn9 = nn.BatchNorm1d(8)
        self.fc1 = nn.Linear(in_dim, 2048)
        self.fc2 = nn.Linear(2048, 1024)
        self.fc3 = nn.Linear(1024, 512)
        self.fc4 = nn.Linear(512, 256)
        self.fc5 = nn.Linear(256, 128)
        self.fc6 = nn.Linear(128, 64)
        self.fc7 = nn.Linear(64, 32)
        self.fc8 = nn.Linear(32, 16)
        self.fc9 = nn.Linear(16, 8)
        self.fc10 = nn.Linear(8, out_dim)
        self.relu = nn.ReLU(inplace=True)


    def forward(self, x):
        sex = self.embed_sex(x[:, 3].long())
        access_freq = self.embed_access_freq(x[:, 4].long())
        multi_a = self.embed_multi_a(x[:, 10].long())
        multi_b = self.embed_multi_b(x[:, 11].long())
        multi_c = self.embed_multi_c(x[:, 12].long())
        multi_d = self.embed_multi_d(x[:, 13].long())
        multi_e = self.embed_multi_e(x[:, 14].long())

        out = torch.cat((x[:, 0:3], x[:, 5:10], x[:, 15:]), dim=1)
        out = torch.cat(
            (out, sex, access_freq, multi_a, multi_b, multi_c, multi_d, multi_e), dim=1)
        
        out = self.fc1(self.bn0(out))
        out = self.fc2(self.relu(self.bn1(out)))
        out = self.fc3(self.relu(self.bn2(out)))
        out = self.fc4(self.relu(self.bn3(out)))
        out = self.fc5(self.relu(self.bn4(out)))
        out = self.fc6(self.relu(self.bn5(out)))
        out = self.fc7(self.relu(self.bn6(out)))
        out = self.fc8(self.relu(self.bn7(out)))
        out = self.fc9(self.relu(self.bn8(out)))
        out = self.fc10(self.relu(self.bn9(out)))
        return out


class MyNet_7_Layer(nn.Module):
    def __init__(self):
        super(MyNet_7_Layer, self).__init__()

        self.embed_sex = nn.Embedding(3, 2)
        self.embed_multi_a = nn.Embedding(2561, 13)
        self.embed_multi_b = nn.Embedding(291, 6)
        self.embed_multi_c = nn.Embedding(428, 7)
        self.embed_multi_d = nn.Embedding(1556, 11)
        self.fc1 = nn.Linear(10 + 2 + 13 + 6 + 7 + 11, 1024)
        self.fc2 = nn.Linear(1024, 512)
        self.fc3 = nn.Linear(512, 256)
        self.fc4 = nn.Linear(256, 128)
        self.fc5 = nn.Linear(128, 64)
        self.fc6 = nn.Linear(64, 16)
        self.fc7 = nn.Linear(16, 2)
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        sex = self.embed_sex(x[:, 0].long())
        multi_a = self.embed_multi_a(x[:, 7].long())
        multi_b = self.embed_multi_b(x[:, 8].long())
        multi_c = self.embed_multi_c(x[:, 9].long())
        multi_d = self.embed_multi_d(x[:, 10].long())

        out = torch.cat((x[:, 2:7], x[:, 11:16]), dim=1)
        out = torch.cat(
            (out, sex, multi_a, multi_b, multi_c, multi_d), dim=1)

        out = self.fc1(out)
        out = F.dropout(out, p=0.5, training=self.training)
        out = self.relu(out)
        out = self.fc2(out)
        out = F.dropout(out, p=0.5, training=self.training)
        out = self.relu(out)
        out = self.fc3(out)
        out = F.dropout(out, p=0.5, training=self.training)
        out = self.relu(out)
        out = self.fc4(out)
        out = F.dropout(out, p=0.5, training=self.training)
        out = self.relu(out)
        out = self.fc5(out)
        out = F.dropout(out, p=0.5, training=self.training)
        out = self.relu(out)
        out = self.fc6(out)
        out = F.dropout(out, p=0.5, training=self.training)
        out = self.relu(out)
        out = self.fc7(out)
        return out


class DS(Dataset):
    def __init__(self):
        x1 = [2, 0.0, 742423, -1.404297, 1.532980, -0.201699, -0.591583, -0.283857, 1486, 170,
              249, 657, 0.343009, -1.265502, 1.161576, 268933, -0.166730, -0.438016]
        x2 = [0, 1.0, 1364057, 0.712100, -0.652324, -0.201699, -0.591583, -0.283857, 1958, 27,
              370, 1252, 0.343009, 2.585447, 1.161576, 29148, -0.166730, 1.313411]
        x3 = [0, 1.0, 1364057, 0.712100, -0.652324, -0.201699, -0.591583, -0.283857, 1958, 27,
              370, 1252, 0.343009, 2.585447, 1.161576, 915753, -0.173304, 1.313411]
        x4 = [0, 0.0, 1364057, 0.712100, -0.652324, -0.201699, -0.591583, -0.283857, 1958, 27,
              370, 1252, 0.343009, 2.585447, 1.161576, 748219, -0.173304, -0.438016]
        self.data = np.array([x1, x2, x3, x4] * 100)

    def __getitem__(self, index):
        return self.data[index], self.data[index][1]

    def __len__(self):
        return len(self.data)


if __name__ == '__main__':
    BATCH_SIZE = 25
    DEVICE = torch.device('cpu')
    EPOCH = 10000
    LR = 0.1
    train_size = 400

    from torch import optim, nn
    from tqdm import tqdm

    data_loader = DataLoader(dataset=DS(), batch_size=BATCH_SIZE, shuffle=True)
    net = MyNet_7_Layer().to(DEVICE)

    loss_function = nn.CrossEntropyLoss()
    optimizer = optim.Adam(net.parameters())
    # scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.75)

    for epoch in range(EPOCH):
        count, running_correct, running_loss = 0, 0, 0

        # with tqdm(total=train_size/BATCH_SIZE) as pbar:
        for step, (bx, by) in enumerate(data_loader):
            # 训练
            bx = bx.float().to(DEVICE)
            by = by.long().to(DEVICE)

            prediction = net(bx)
            loss = loss_function(prediction, by)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # 统计成效
            pre = torch.argmax(torch.softmax(prediction, dim=1), dim=1)
            my_loss = float(loss.data.cpu().numpy())
            my_correct = sum(pre.cpu().numpy() == by.cpu().numpy())
            my_acc = my_correct / BATCH_SIZE
            count += 1
            running_loss += my_loss
            running_correct += my_correct

            # 更新进度条
            # pbar.update(1)
            # pbar.set_description('Epoch: %d, Loss: %.4f, Acc: %.4f' % (
            #                       epoch,
            #                       my_loss,
            #                       my_acc))

        # 输出一轮结果
        print('Epoch: %d, Loss: %.4f, Acc: %.4f, Lr: %.5f' % (
            epoch,
            running_loss / count,
            running_correct / train_size,
            optimizer.state_dict()['param_groups'][0]['lr']))

        # 保存参数
        # torch.save(net.state_dict(), PKL_DIR_OUT)

        # lr scheduler
        # scheduler.step()
