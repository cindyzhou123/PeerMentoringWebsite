// for global style consistency
import "fontsource-raleway/latin-500-normal.css";

export interface themeProps {
    color:{
        background: string;
        primaryGreen: string;
        secondaryGreen: string;
        textWhite: string;
        textBlue: string;
        textGrey: string;
    }
    font:{
        family: string;
    }
}

export const theme:themeProps = {
    color:{
        background: '#F7F7F2',
        primaryGreen: '#899878',
        secondaryGreen: '#E4E6C3',
        textWhite: '#F7F7F2',
        textBlue: '#4F56FF',
        textGrey: '#696969'
    },
    font: {
        family: 'Raleway'
    }
}

export default theme;