import styled from 'styled-components';
import theme from '../../styles';

interface TextOverrideProps {

}

const baseFontStyles = (props: TextOverrideProps) => ({
    fontFamily: theme.font.family
})

const p = styled.p<TextOverrideProps>(props => ({
    ...baseFontStyles(props),
}));
  
const h1 = styled.h1<TextOverrideProps>(props => ({
    ...baseFontStyles(props),
}));
  
const h2 = styled.h2<TextOverrideProps>(props => ({
    ...baseFontStyles(props),
}));
  
const h3 = styled.h3<TextOverrideProps>(props => ({
    ...baseFontStyles(props),
}));
  
const h4 = styled.h4<TextOverrideProps>(props => ({
    ...baseFontStyles(props),
}));

const h5 = styled.h5<TextOverrideProps>(props => ({
    ...baseFontStyles(props),
}));
  
const h6 = styled.h6<TextOverrideProps>(props => ({
    ...baseFontStyles(props),
}));
  
export const Text = {
    p, h1, h2, h3, h4, h5, h6
};
  
export default Text;