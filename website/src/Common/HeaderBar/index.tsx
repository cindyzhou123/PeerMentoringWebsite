import React from "react";
import {HeaderBarContainer} from './headerBar.styles';

import {Text} from '../Text';


interface HeaderBarProps{

}

export const HeaderBar: React.FC<HeaderBarProps> = (props) => {
    return (
        <HeaderBarContainer>
            <Text.h1>header 1</Text.h1>
            <Text.h2>header 2</Text.h2>
            <Text.h3>header 3</Text.h3>
            <Text.h4>header 4</Text.h4>
            <Text.h5>header 5</Text.h5>
            <Text.h6>header 6</Text.h6>
            <Text.p>paragraph</Text.p>
        </HeaderBarContainer>
    );
};

export default HeaderBar;