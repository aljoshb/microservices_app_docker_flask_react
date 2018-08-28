import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer'

import UsersList from '../UsersList';

const users = [
    {
        'active': true,
        'email': 'bolualawode@gmail.com',
        'id': 1,
        'username': 'josh'
    },
    {
        'active': true,
        'email': 'jon@doe.com',
        'id': 2,
        'username': 'jondoe'
    }
];

test('UsersList renders properly', () => {
    const wrapper = shallow(<UsersList users={users}/>);
    const element = wrapper.find('h4');
    expect(element.length).toBe(2);
    expect(element.get(0).props.children).toBe('josh');
});

test('UsersList renders a snapshot properly', () => {
    const tree = renderer.create(<UsersList users={users}/>).toJSON();
    expect(tree).toMatchSnapshot();
});